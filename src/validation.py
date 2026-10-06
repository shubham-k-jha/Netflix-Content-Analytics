"""Strict source and analytical validation contracts."""
from __future__ import annotations
import pandas as pd

GLOBAL_COLS = {"week","category","weekly_rank","show_title","season_title","weekly_hours_viewed","runtime","weekly_views","cumulative_weeks_in_top_10"}
COUNTRY_COLS = {"country_name","country_iso2","week","category","weekly_rank","show_title","season_title","cumulative_weeks_in_top_10"}
ALLTIME_COLS = {"category","rank","show_title","season_title","hours_viewed_first_91_days","runtime","views_first_91_days"}
TMDB_REQUIRED = {"id","title","type"}


def _require(df, cols, name):
    missing = sorted(set(cols) - set(df.columns))
    if missing:
        raise ValueError(f"{name}: missing columns {missing}")


def _numeric_nonnegative(df, cols, name):
    for col in cols:
        x = pd.to_numeric(df[col], errors="coerce")
        if x.dropna().lt(0).any():
            raise ValueError(f"{name}: negative values in {col}")


def validate_global(df):
    _require(df, GLOBAL_COLS, "global_weekly")
    if pd.to_datetime(df.week, errors="coerce").isna().any(): raise ValueError("global_weekly: invalid week")
    if df.weekly_rank.isna().any() or df.weekly_rank.lt(1).any() or df.weekly_rank.gt(10).any(): raise ValueError("global_weekly: rank must be 1..10")
    if df.show_title.isna().any(): raise ValueError("global_weekly: null show_title")
    _numeric_nonnegative(df, ["weekly_hours_viewed","weekly_views","runtime","cumulative_weeks_in_top_10"], "global_weekly")
    if df.duplicated(["week","category","weekly_rank"]).any(): raise ValueError("global_weekly: duplicate grain")
    return True


def validate_country(df):
    _require(df, COUNTRY_COLS, "country_weekly")
    if pd.to_datetime(df.week, errors="coerce").isna().any(): raise ValueError("country_weekly: invalid week")
    if df.weekly_rank.isna().any() or df.weekly_rank.lt(1).any() or df.weekly_rank.gt(10).any(): raise ValueError("country_weekly: rank must be 1..10")
    if df.country_iso2.isna().any(): raise ValueError("country_weekly: null country_iso2")
    if df.country_iso2.astype(str).str.len().ne(2).any(): raise ValueError("country_weekly: country_iso2 must be 2 chars")
    if df.duplicated(["country_iso2","week","category","weekly_rank"]).any(): raise ValueError("country_weekly: duplicate grain")
    return True


def validate_alltime(df, name="global_alltime"):
    _require(df, ALLTIME_COLS, name)
    if df.duplicated(["category","rank"]).any(): raise ValueError(f"{name}: duplicate category/rank")
    if df["rank"].isna().any() or df["rank"].lt(1).any() or df["rank"].gt(10).any(): raise ValueError(f"{name}: rank must be 1..10")
    _numeric_nonnegative(df,["hours_viewed_first_91_days","runtime","views_first_91_days"],name)
    return True


def validate_tmdb(df):
    _require(df, TMDB_REQUIRED, "tmdb_legacy")
    if df.title.isna().any() or df.type.isna().any(): raise ValueError("tmdb_legacy: null title/type")
    return True


def validate_alias_equal(a: pd.DataFrame, b: pd.DataFrame, name_a: str, name_b: str):
    if list(a.columns) != list(b.columns):
        raise ValueError(f"Alias mismatch: {name_a} and {name_b} have different columns")
    if len(a) != len(b) or not a.equals(b):
        raise ValueError(f"Alias mismatch: {name_a} and {name_b} are not exact duplicates")
    return True
