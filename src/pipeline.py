"""Authoritative end-to-end Netflix Top 10 pipeline.

Raw sources -> validation -> normalized facts -> enrichment -> analytical marts -> SQLite.
Run from the repository root with: python -m src.pipeline
"""
from __future__ import annotations

import hashlib
import json
import logging
import re
import shutil
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd

from .config import PIPELINE_VERSION, RAW, PROC, REPORTS, SOURCE_FILES, ROOT
from .validation import validate_global, validate_country, validate_alltime, validate_tmdb, validate_alias_equal

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
log = logging.getLogger("netflix.pipeline")


PLACEHOLDER_SEASONS = {"", "n/a", "na", "nan", "none", "null"}


def normalize_key(value: object):
    if pd.isna(value):
        return np.nan
    s = str(value).strip().lower()
    if s in PLACEHOLDER_SEASONS:
        return np.nan
    s = re.sub(r"[^\w]+", " ", s, flags=re.UNICODE)
    s = re.sub(r"\s+", " ", s).strip()
    return s or np.nan


def add_identity_columns(df: pd.DataFrame) -> pd.DataFrame:
    x = df.copy()
    x["title_key"] = x["show_title"].map(normalize_key)
    x["season_key"] = x["season_title"].map(normalize_key)
    x["content_type"] = np.where(x["category"].astype(str).str.startswith("Films"), "Film", "TV")
    season_part = x["season_key"].fillna("")
    x["title_family_key"] = x["title_key"] + " | " + x["content_type"].str.lower() + np.where(season_part.eq(""), "", " | " + season_part)
    category_key = x["category"].map(normalize_key).fillna("")
    x["entity_key"] = x["title_family_key"] + " | " + category_key
    return x


def prepare_tmdb(tmdb: pd.DataFrame) -> pd.DataFrame:
    t = tmdb.copy()
    t["title_key"] = t["title"].map(normalize_key)
    t["content_type"] = np.where(t["type"].astype(str).str.lower().eq("tv"), "TV", "Film")
    t["release_date"] = pd.to_datetime(t["release_date"], errors="coerce")
    t["id"] = pd.to_numeric(t["id"], errors="coerce")
    t["_score"] = t["release_date"].notna().astype(int) + t["id"].notna().astype(int)
    t = t.sort_values(["title_key","content_type","_score","id"], ascending=[True,True,False,True], na_position="last")
    t = t.drop_duplicates(["title_key","content_type"], keep="first")
    return t.drop(columns="_score")


def enrich_global(raw: pd.DataFrame, tmdb: pd.DataFrame) -> pd.DataFrame:
    x = add_identity_columns(raw)
    x["week"] = pd.to_datetime(x["week"], errors="raise")
    x["weekly_rank"] = pd.to_numeric(x["weekly_rank"], errors="raise")
    for col in ["weekly_hours_viewed","weekly_views","runtime","cumulative_weeks_in_top_10"]:
        x[col] = pd.to_numeric(x[col], errors="coerce")

    # Enrichment is reference metadata only. A title may have multiple TMDB candidates;
    # deterministic deduplication happens in prepare_tmdb.
    tcols = ["title_key","content_type","id","adult","budget","genres","original_language","original_title","overview",
             "popularity","poster_path","production_companies","production_countries","release_date","revenue","spoken_languages","runtime"]
    x = x.merge(tmdb[tcols], on=["title_key","content_type"], how="left", suffixes=("","_tmdb"))
    x.rename(columns={"runtime_tmdb":"runtime_tmdb"}, inplace=True)
    x["runtime_tmdb"] = pd.to_numeric(x["runtime_tmdb"], errors="coerce")

    x["week_year"] = x.week.dt.year
    x["week_month"] = x.week.dt.month
    x["weekofyear"] = x.week.dt.isocalendar().week.astype(int)
    x["rank_score"] = (11 - x.weekly_rank).clip(lower=0)
    x["log_views"] = np.log1p(x.weekly_views)
    x["log_hours"] = np.log1p(x.weekly_hours_viewed)
    x["views_per_hour"] = x.weekly_views / x.weekly_hours_viewed.replace(0, np.nan)
    x["content_age_days"] = (x.week - x.release_date).dt.days
    x["content_age_years"] = x.content_age_days / 365.25
    x["release_age_group"] = pd.cut(x.content_age_years, [-np.inf,1,3,5,10,np.inf], labels=["<1y","1-3y","3-5y","5-10y","10y+"]).astype(object)
    x.loc[x.content_age_years < 0, "release_age_group"] = "Pre-release/metadata"
    x["tmdb_matched"] = x["id"].notna()

    x = x.sort_values(["entity_key","week","category","weekly_rank"]).reset_index(drop=True)
    grp = x.groupby("entity_key", sort=False)
    x["prev_views"] = grp["weekly_views"].shift(1)
    x["prev_rank"] = grp["weekly_rank"].shift(1)
    x["prev_week"] = grp["week"].shift(1)
    x["views_wow_pct"] = x.weekly_views / x.prev_views.replace(0,np.nan) - 1
    x["rank_change"] = x.prev_rank - x.weekly_rank
    x["is_continuing_from_prev_week"] = (x.week - x.prev_week).dt.days.eq(7)
    x.loc[~x.is_continuing_from_prev_week, ["prev_views","prev_rank","views_wow_pct","rank_change"]] = np.nan
    x["next_views"] = grp["weekly_views"].shift(-1)
    x["next_week"] = grp["week"].shift(-1)
    x["is_continuing_next_week"] = (x.next_week - x.week).dt.days.eq(7)
    x.loc[~x.is_continuing_next_week, "next_views"] = np.nan
    return x.sort_values(["week","category","weekly_rank"]).reset_index(drop=True)


def enrich_country(raw: pd.DataFrame, tmdb: pd.DataFrame) -> pd.DataFrame:
    x = add_identity_columns(raw)
    x["week"] = pd.to_datetime(x["week"], errors="raise")
    x["weekly_rank"] = pd.to_numeric(x["weekly_rank"], errors="raise")
    x["cumulative_weeks_in_top_10"] = pd.to_numeric(x["cumulative_weeks_in_top_10"], errors="coerce")
    tcols = ["title_key","content_type","id","genres","original_language","production_countries","release_date","popularity","runtime"]
    t = tmdb[tcols].copy()
    x = x.merge(t, on=["title_key","content_type"], how="left", suffixes=("","_tmdb"))
    x["release_date"] = pd.to_datetime(x["release_date"], errors="coerce")
    x["runtime_tmdb"] = pd.to_numeric(x["runtime"], errors="coerce")
    x.drop(columns=["runtime"], inplace=True)
    x["tmdb_matched"] = x["id"].notna()
    return x.sort_values(["country_iso2","week","category","weekly_rank"]).reset_index(drop=True)


def build_entity_performance(g: pd.DataFrame, c: pd.DataFrame) -> pd.DataFrame:
    def sum_min(s):
        return s.sum(min_count=1)
    agg = g.groupby("entity_key", dropna=False).agg(
        title_family_key=("title_family_key","first"), show_title=("show_title","first"), content_type=("content_type","first"),
        first_week=("week","min"), last_week=("week","max"), weeks_observed=("week","nunique"),
        peak_rank=("weekly_rank","min"), avg_rank=("weekly_rank","mean"),
        peak_views=("weekly_views","max"), peak_hours=("weekly_hours_viewed","max"),
        total_views=("weekly_views",sum_min), total_hours=("weekly_hours_viewed",sum_min),
        max_cumulative_weeks=("cumulative_weeks_in_top_10","max"), runtime=("runtime","first"),
        tmdb_matched=("tmdb_matched","max"), tmdb_popularity=("popularity","max"), tmdb_revenue=("revenue","max"),
        release_date=("release_date","first"),
    ).reset_index()
    reach = c.groupby("title_family_key")["country_iso2"].nunique().rename("country_reach")
    agg = agg.merge(reach, left_on="title_family_key", right_index=True, how="left")
    agg["country_reach"] = agg.country_reach.fillna(0).astype(int)
    peak_rows = g.sort_values(["entity_key","weekly_rank","week"]).drop_duplicates("entity_key")[["entity_key","week"]].rename(columns={"week":"peak_week"})
    agg = agg.merge(peak_rows, on="entity_key", how="left")
    agg["weeks_to_peak"] = ((agg.peak_week - agg.first_week).dt.days / 7).round().astype("Int64")
    agg["longevity_weeks_observed"] = agg.weeks_observed.astype(int)
    agg["elapsed_weeks"] = ((agg.last_week - agg.first_week).dt.days // 7 + 1).astype(int)
    agg["performance_tier"] = pd.cut(agg.longevity_weeks_observed,[0,1,2,4,np.inf],labels=["1 week","2 weeks","3-4 weeks","5+ weeks"],include_lowest=True).astype(str)
    agg.drop(columns=["peak_week"], inplace=True)
    return agg


def build_survival_curve(e: pd.DataFrame, max_week: pd.Timestamp) -> pd.DataFrame:
    d = e[["entity_key","elapsed_weeks","last_week"]].copy()
    d["event"] = (pd.to_datetime(d.last_week) < max_week).astype(int)
    rows=[]; survival=1.0
    for t in sorted(d.elapsed_weeks.unique()):
        at_risk = int((d.elapsed_weeks >= t).sum())
        events = int(((d.elapsed_weeks == t) & (d.event == 1)).sum())
        if at_risk:
            survival *= (1 - events / at_risk)
        rows.append({"duration_week":int(t),"events":events,"at_risk":at_risk,"survival_probability":survival})
    return pd.DataFrame(rows)


def make_h1_2026_table() -> pd.DataFrame:
    rows = [
        ("Film",1,"War Machine","",147),("Film",2,"The Rip","",136),("Film",3,"Swapped","",131),("Film",4,"KPop Demon Hunters","",130),("Film",5,"Apex","",129),("Film",6,"Thrash","",100),("Film",7,"People We Meet on Vacation","",78),("Film",8,"The Crash","",65),("Film",9,"Peaky Blinders: The Immortal Man","",64),("Film",10,"Office Romance","",58),
        ("TV",1,"His & Hers","",104),("TV",2,"Bridgerton","Season 4",100),("TV",3,"I Will Find You","",64),("TV",4,"Stranger Things","Season 5",56),("TV",5,"Run Away","",50),("TV",6,"Teach You a Lesson","",48),("TV",7,"One Piece","Season 2",47),("TV",8,"Man on Fire","Season 1",40),("TV",9,"Ms. Rachel","Season 1",37),("TV",10,"The Night Agent","Season 3",36),
    ]
    df = pd.DataFrame(rows, columns=["content_type","rank","title","season_title","views_millions"])
    df["report_period"] = "2026 H1"
    df["source"] = "Netflix What We Watched H1 2026 supplied report images"
    return df


def load_and_validate():
    required = [SOURCE_FILES[k] for k in ["global_weekly","country_weekly","global_weekly_snapshot","global_alltime","popular_weekly_snapshot","popular_alltime_snapshot","tmdb_legacy"]]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    if missing: raise FileNotFoundError(f"Missing required sources: {missing}")
    g = pd.read_csv(SOURCE_FILES["global_weekly"], sep="\t", low_memory=False)
    c = pd.read_csv(SOURCE_FILES["country_weekly"], sep="\t", low_memory=False)
    gs = pd.read_csv(SOURCE_FILES["global_weekly_snapshot"], sep="\t", low_memory=False)
    a = pd.read_csv(SOURCE_FILES["global_alltime"], sep="\t", low_memory=False)
    ps = pd.read_csv(SOURCE_FILES["popular_weekly_snapshot"], sep="\t", low_memory=False)
    pa = pd.read_csv(SOURCE_FILES["popular_alltime_snapshot"], sep="\t", low_memory=False)
    t = pd.read_csv(SOURCE_FILES["tmdb_legacy"], low_memory=False)
    validate_global(g); validate_global(gs); validate_country(c); validate_alltime(a); validate_alltime(pa); validate_tmdb(t)
    validate_alias_equal(g, gs, "all-weeks-global.tsv", "2026-10-05_global_weekly.tsv")
    validate_alias_equal(g, ps, "all-weeks-global.tsv", "most-popular_global_weekly.tsv")
    validate_alias_equal(a, pa, "2026-10-05_global_alltime.tsv", "most-popular_global_alltime.tsv")
    if not a.equals(pa): raise ValueError("Most-popular all-time aliases disagree")
    return {"global":g,"country":c,"alltime":a,"tmdb":t}


def write_database(g,c,a,tmdb,e,survival,h1,source_registry):
    db = PROC / "netflix_analytics.db"
    if db.exists(): db.unlink()
    con = sqlite3.connect(db)
    tables = {
        "global_weekly":g, "country_weekly":c, "most_popular":a, "tmdb_metadata":tmdb,
        "entity_performance":e, "survival_curve":survival, "h1_2026_most_watched":h1, "source_registry":source_registry,
    }
    for name, df in tables.items(): df.to_sql(name, con, if_exists="replace", index=False)
    indexes = [
        "CREATE INDEX idx_global_entity_week ON global_weekly(entity_key, week)",
        "CREATE INDEX idx_global_week_category_rank ON global_weekly(week, category, weekly_rank)",
        "CREATE INDEX idx_country_entity_week ON country_weekly(entity_key, week)",
        "CREATE INDEX idx_country_iso_week ON country_weekly(country_iso2, week)",
    ]
    for sql in indexes:
        con.execute(sql)
    con.commit(); con.close()


def sha256_file(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""): h.update(chunk)
    return h.hexdigest()


def clean_generated():
    for p in (PROC, REPORTS):
        if p.exists(): shutil.rmtree(p)
        p.mkdir(parents=True, exist_ok=True)


def build():
    clean_generated()
    raw = load_and_validate()
    tmdb = prepare_tmdb(raw["tmdb"])
    g = enrich_global(raw["global"], tmdb)
    c = enrich_country(raw["country"], tmdb)
    a = raw["alltime"].copy()
    a["content_type"] = np.where(a.category.astype(str).str.startswith("Films"),"Film","TV")
    a["title_key"] = a.show_title.map(normalize_key)
    a["season_key"] = a.season_title.map(normalize_key)
    a["title_family_key"] = a.title_key + " | " + a.content_type.str.lower() + np.where(a.season_key.fillna("").eq(""),""," | "+a.season_key)
    a["entity_key"] = a.title_family_key + " | " + a.category.map(normalize_key).fillna("")
    e = build_entity_performance(g,c)
    survival = build_survival_curve(e,g.week.max())
    h1 = make_h1_2026_table()
    source_registry = pd.DataFrame([
        {"source_key":"global_weekly","path":"data/raw/all-weeks-global.tsv","role":"authoritative global weekly fact","rows":len(raw["global"]),"min_week":raw["global"].week.min(),"max_week":raw["global"].week.max()},
        {"source_key":"country_weekly","path":"data/raw/all-weeks-countries.tsv","role":"authoritative country weekly fact","rows":len(raw["country"]),"min_week":raw["country"].week.min(),"max_week":raw["country"].week.max()},
        {"source_key":"global_alltime","path":"data/raw/2026-10-05_global_alltime.tsv","role":"authoritative current Most Popular snapshot","rows":len(a),"min_week":None,"max_week":None},
        {"source_key":"global_weekly_snapshot_alias","path":"data/raw/2026-10-05_global_weekly.tsv","role":"verified exact duplicate of global weekly","rows":len(raw["global"]),"min_week":raw["global"].week.min(),"max_week":raw["global"].week.max()},
        {"source_key":"popular_weekly_snapshot_alias","path":"data/raw/most-popular_global_weekly.tsv","role":"verified exact duplicate of global weekly; not counted separately","rows":len(raw["global"]),"min_week":raw["global"].week.min(),"max_week":raw["global"].week.max()},
        {"source_key":"popular_alltime_snapshot_alias","path":"data/raw/most-popular_global_alltime.tsv","role":"verified exact duplicate of current all-time snapshot","rows":len(a),"min_week":None,"max_week":None},
        {"source_key":"tmdb_legacy","path":"data/raw/tmdb_data_legacy_2023.csv","role":"optional external metadata enrichment; not Netflix performance","rows":int(len(raw["tmdb"])),"min_week":None,"max_week":None},
        {"source_key":"h1_2026_report_assets","path":"assets/NFLX_H12026_EngagementReport_Top10*.png","role":"supplied visual cross-check; manually transcribed to h1_2026_most_watched","rows":20,"min_week":None,"max_week":None},
    ])
    # Dates are strings in registry for SQLite portability.
    for col in ["min_week","max_week"]: source_registry[col] = source_registry[col].astype(str).replace("NaT","")
    g.to_csv(PROC/"global_analytics.csv",index=False)
    c.to_csv(PROC/"country_analytics.csv",index=False)
    a.to_csv(PROC/"most_popular.csv",index=False)
    tmdb.to_csv(PROC/"tmdb_metadata.csv",index=False)
    e.to_csv(PROC/"entity_performance.csv",index=False)
    survival.to_csv(PROC/"survival_curve.csv",index=False)
    h1.to_csv(PROC/"h1_2026_most_watched.csv",index=False)
    source_registry.to_csv(REPORTS/"source_registry.csv",index=False)
    alias_report = {
        "global_weekly_aliases": {
            "2026-10-05_global_weekly.tsv": "exact_duplicate_of_all-weeks-global.tsv",
            "most-popular_global_weekly.tsv": "exact_duplicate_of_all-weeks-global.tsv"
        },
        "alltime_aliases": {
            "most-popular_global_alltime.tsv": "exact_duplicate_of_2026-10-05_global_alltime.tsv"
        },
        "counts_as_unique_facts": {"global_weekly": True, "country_weekly": True, "global_alltime": True, "global_weekly_aliases": False, "alltime_aliases": False},
        "h1_2026_archive_preserved": True
    }
    (REPORTS/"source_alias_validation.json").write_text(json.dumps(alias_report,indent=2),encoding="utf-8")
    write_database(g,c,a,tmdb,e,survival,h1,source_registry)
    tmdb_row_rate = float(g.tmdb_matched.mean()*100)
    tmdb_title_rate = float(g[["entity_key","tmdb_matched"]].drop_duplicates("entity_key").tmdb_matched.mean()*100)
    summary = {
        "pipeline_version":PIPELINE_VERSION,"global_rows":len(g),"country_rows":len(c),"entity_rows":len(e),"countries":int(c.country_iso2.nunique()),"weeks":int(g.week.nunique()),
        "global_min_week":str(g.week.min().date()),"global_max_week":str(g.week.max().date()),"views_coverage_pct":float(g.weekly_views.notna().mean()*100),"runtime_coverage_pct":float(g.runtime.notna().mean()*100),
        "tmdb_row_match_pct":tmdb_row_rate,"tmdb_entity_match_pct":tmdb_title_rate,"alltime_rows":len(a),"h1_2026_rows":len(h1),
    }
    (REPORTS/"pipeline_base_summary.json").write_text(json.dumps(summary,indent=2),encoding="utf-8")
    return summary, g, c, a, tmdb, e, survival, h1, source_registry


def write_manifest(summary):
    raw_files={}
    for p in sorted(RAW.glob("*")):
        if p.is_file(): raw_files[str(p.relative_to(ROOT))]={"bytes":p.stat().st_size,"sha256":sha256_file(p)}
    code_files={}
    for base in (ROOT/"src", ROOT/"scripts", ROOT/"dashboard", ROOT/"tests"):
        if base.exists():
            for p in sorted(base.rglob("*.py")):
                code_files[str(p.relative_to(ROOT))]={"bytes":p.stat().st_size,"sha256":sha256_file(p)}
    asset_files={}
    for p in sorted((ROOT/"assets").glob("*")):
        if p.is_file(): asset_files[str(p.relative_to(ROOT))]={"bytes":p.stat().st_size,"sha256":sha256_file(p)}
    outputs={}
    for base in (PROC,REPORTS):
        for p in sorted(base.rglob("*")):
            if p.is_file() and p.name != "pipeline_run_manifest.json": outputs[str(p.relative_to(ROOT))]={"bytes":p.stat().st_size,"sha256":sha256_file(p)}
    manifest={"pipeline_version":PIPELINE_VERSION,"source_files":raw_files,"code_files":code_files,"asset_files":asset_files,"output_files":outputs,"summary":summary,"deterministic_build":True}
    (REPORTS/"pipeline_run_manifest.json").write_text(json.dumps(manifest,indent=2,sort_keys=True),encoding="utf-8")


if __name__ == "__main__":
    summary,*_ = build()
    log.info("Base pipeline complete: %s",summary)
    write_manifest(summary)
