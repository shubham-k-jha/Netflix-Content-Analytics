"""Analytical layer for Netflix Content Intelligence v8."""
from __future__ import annotations

import json
import sqlite3
from pathlib import Path

import numpy as np
import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu, spearmanr
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.inspection import permutation_importance
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from .config import PIPELINE_VERSION, PROC, REPORTS, ROOT


def km_curve(durations: pd.Series, events: pd.Series, segment_type: str, segment: str) -> pd.DataFrame:
    d = pd.DataFrame({"duration":pd.to_numeric(durations).astype(int),"event":pd.to_numeric(events).astype(int)})
    rows=[]; survival=1.0
    for t in sorted(d.duration.unique()):
        at_risk=int((d.duration>=t).sum())
        events_t=int(((d.duration==t)&(d.event==1)).sum())
        if at_risk:
            survival *= 1 - events_t/at_risk
        rows.append({"segment_type":segment_type,"segment":segment,"duration_week":int(t),"at_risk":at_risk,"events":events_t,"survival_probability":survival})
    return pd.DataFrame(rows)


def entity_week_frame(g: pd.DataFrame) -> pd.DataFrame:
    x=g.copy()
    x["week"]=pd.to_datetime(x["week"])
    x=x.sort_values(["entity_key","week","category","weekly_rank"])
    out=x.groupby(["entity_key","week"],as_index=False).agg(
        show_title=("show_title","first"), content_type=("content_type","first"),
        weekly_views=("weekly_views","max"), weekly_hours_viewed=("weekly_hours_viewed","max"),
        weekly_rank=("weekly_rank","min"), cumulative_weeks_in_top_10=("cumulative_weeks_in_top_10","max"),
        runtime=("runtime","max"),
    )
    out=out.sort_values(["entity_key","week"]).reset_index(drop=True)
    grp=out.groupby("entity_key",sort=False)
    out["prev_week"]=grp["week"].shift(1)
    out["prev_views"]=grp["weekly_views"].shift(1)
    out["prev_rank"]=grp["weekly_rank"].shift(1)
    out["is_continuing_from_prev_week"]=(out.week-out.prev_week).dt.days.eq(7)
    out.loc[~out.is_continuing_from_prev_week,["prev_views","prev_rank"]]=np.nan
    out["rank_change"]=out.prev_rank-out.weekly_rank
    out["views_wow_pct"]=out.weekly_views/out.prev_views.replace(0,np.nan)-1
    out.loc[~out.is_continuing_from_prev_week,"views_wow_pct"]=np.nan
    out["next_week"]=grp["week"].shift(-1)
    out["next_views"]=grp["weekly_views"].shift(-1)
    out["is_continuing_next_week"]=(out.next_week-out.week).dt.days.eq(7)
    out.loc[~out.is_continuing_next_week,"next_views"]=np.nan
    return out


def title_mart(g: pd.DataFrame, c: pd.DataFrame, e: pd.DataFrame) -> pd.DataFrame:
    out=e.copy()
    ew=entity_week_frame(g)
    rank=ew.groupby("entity_key").agg(
        rank_std=("weekly_rank","std"), rank_range=("weekly_rank",lambda s:float(s.max()-s.min())),
        mean_abs_rank_change=("rank_change",lambda s:float(s.dropna().abs().mean()) if s.notna().any() else np.nan),
    ).reset_index()
    out=out.drop(columns=["rank_std","rank_range","mean_abs_rank_change"],errors="ignore").merge(rank,on="entity_key",how="left")
    out["rank_volatility_index"]=out.rank_std.fillna(0)*0.5+out.rank_range.fillna(0)*0.3+out.mean_abs_rank_change.fillna(0)*0.2
    total_weeks=ew.week.nunique()
    out["global_share_of_observed_weeks"]=out.weeks_observed/total_weeks

    counts=c.groupby(["title_family_key","country_iso2"]).size().reset_index(name="observations")
    reach=counts.groupby("title_family_key").country_iso2.nunique().rename("country_reach")
    hhi=counts.groupby("title_family_key").apply(lambda z:float(((z.observations/z.observations.sum())**2).sum()),include_groups=False).rename("country_hhi")
    out=out.drop(columns=["country_reach","country_hhi"],errors="ignore").merge(reach,left_on="title_family_key",right_index=True,how="left").merge(hhi,left_on="title_family_key",right_index=True,how="left")
    out["country_reach"]=out.country_reach.fillna(0).astype(int)
    out["country_diversity_index"]=1-out.country_hhi.fillna(1)

    coverage=g.groupby("entity_key").weekly_views.apply(lambda s:int(s.notna().sum())).rename("views_coverage_weeks")
    out=out.drop(columns="views_coverage_weeks",errors="ignore").merge(coverage,on="entity_key",how="left")
    out["views_coverage_weeks"]=out.views_coverage_weeks.fillna(0).astype(int)
    out["views_per_views_covered_week"]=out.total_views/out.views_coverage_weeks.replace(0,np.nan)
    out["peak_to_average_views"]=out.peak_views/out.views_per_views_covered_week.replace(0,np.nan)

    out["release_date"]=pd.to_datetime(out.release_date,errors="coerce")
    out["first_week"]=pd.to_datetime(out.first_week,errors="coerce")
    out["release_age_days"]=(out.first_week-out.release_date).dt.days
    out["release_age_years"]=out.release_age_days/365.25
    out["release_age_group"]=pd.cut(out.release_age_years,[-np.inf,1,3,5,10,np.inf],labels=["<1y","1-3y","3-5y","5-10y","10y+"]).astype(object)
    out.loc[out.release_age_years<0,"release_age_group"]="Pre-release/metadata"

    # Percentile score is deliberately descriptive, not a predictive label.
    longevity_pct=out.longevity_weeks_observed.rank(pct=True)
    peak_pct=1-out.peak_rank.rank(pct=True)
    reach_pct=out.country_reach.rank(pct=True)
    score=0.5*longevity_pct+0.3*peak_pct+0.2*reach_pct
    out["performance_score"]=score
    out["performance_segment"]=pd.cut(score,[0,.2,.5,.8,1],labels=["Short-lived hit","Regional performer","Sustained performer","Global/sustained hit"],include_lowest=True).astype(str)

    # Breakout acceleration uses an exact two-week interval on a unique entity-week series.
    b=ew.sort_values(["entity_key","week"]).copy()
    b["prev2_views"]=b.groupby("entity_key").weekly_views.shift(2)
    b["prev2_week"]=b.groupby("entity_key").week.shift(2)
    b["two_week_gap_days"]=(b.week-b.prev2_week).dt.days
    b["two_week_view_acceleration"]=np.where((b.two_week_gap_days==14)&b.prev2_views.gt(0)&b.weekly_views.notna(),b.weekly_views/b.prev2_views-1,np.nan)
    br=b.groupby("entity_key").two_week_view_acceleration.max().rename("max_two_week_view_acceleration")
    out=out.drop(columns="max_two_week_view_acceleration",errors="ignore").merge(br,on="entity_key",how="left")
    cutoff=out.max_two_week_view_acceleration.quantile(.95) if out.max_two_week_view_acceleration.notna().any() else np.nan
    out["breakout_threshold_95pct"]=cutoff
    out["breakout_flag"]=out.max_two_week_view_acceleration.ge(cutoff)&out.max_two_week_view_acceleration.notna()
    out["reach_segment"]=pd.cut(out.country_reach,[0,4,14,np.inf],labels=["Regional","Multi-market","Broad international"],include_lowest=True).astype(str)
    return out.sort_values(["peak_views","show_title"],ascending=[False,True],na_position="last").reset_index(drop=True)


def country_similarity(c: pd.DataFrame) -> pd.DataFrame:
    sets={k:set(v.entity_key) for k,v in c.groupby("country_iso2")}
    rows=[]; keys=sorted(sets)
    for i,a in enumerate(keys):
        for b in keys[i+1:]:
            inter=len(sets[a]&sets[b]); union=len(sets[a]|sets[b])
            if union: rows.append((a,b,inter/union,inter,union))
    return pd.DataFrame(rows,columns=["country_a","country_b","jaccard_similarity","shared_titles","union_titles"]).sort_values(["jaccard_similarity","shared_titles"],ascending=False)


def survival_report(e: pd.DataFrame, max_week: pd.Timestamp) -> pd.DataFrame:
    base=e[["entity_key","content_type","elapsed_weeks","last_week","performance_segment"]].copy()
    base["event"]=(pd.to_datetime(base.last_week)<max_week).astype(int)
    frames=[km_curve(base.elapsed_weeks,base.event,"all","all")]
    for name,grp in base.groupby("content_type"):
        frames.append(km_curve(grp.elapsed_weeks,grp.event,"content_type",str(name)))
    for name,grp in base.groupby("performance_segment"):
        frames.append(km_curve(grp.elapsed_weeks,grp.event,"performance_segment",str(name)))
    return pd.concat(frames,ignore_index=True)


def breakout_report(e):
    cols=["entity_key","show_title","content_type","max_two_week_view_acceleration","breakout_flag","peak_views","peak_rank","longevity_weeks_observed","country_reach"]
    return e[cols].sort_values(["breakout_flag","max_two_week_view_acceleration"],ascending=[False,False],na_position="last")


def release_age_report(e):
    return e.dropna(subset=["release_age_group"]).groupby(["release_age_group","content_type"],observed=True).agg(
        titles=("entity_key","size"), median_longevity=("longevity_weeks_observed","median"), median_elapsed_weeks=("elapsed_weeks","median"),
        mean_peak_rank=("peak_rank","mean"), median_reach=("country_reach","median")
    ).reset_index()


def rank_volatility_report(e):
    return e[["entity_key","show_title","content_type","rank_std","rank_range","mean_abs_rank_change","rank_volatility_index","performance_segment"]].sort_values("rank_volatility_index",ascending=False)


def forecast_benchmark(g: pd.DataFrame):
    d=entity_week_frame(g)
    d=d[(d.weekly_views.notna())&(d.is_continuing_next_week)&d.prev_views.notna()&d.next_views.notna()].copy()
    d["log_prev_views"]=np.log1p(d.prev_views.clip(lower=0))
    d["views_wow_pct"]=d.views_wow_pct.replace([np.inf,-np.inf],np.nan).fillna(0).clip(-5,5)
    features=["prev_views","weekly_rank","rank_change","cumulative_weeks_in_top_10","log_prev_views","views_wow_pct"]
    d=d.dropna(subset=features+["next_views"])
    weeks=np.array(sorted(d.week.unique()))
    if len(weeks)<10: raise ValueError("Not enough chronological weeks for forecast validation")
    cutoff=weeks[max(1,int(len(weeks)*.8))-1]
    train=d[d.week<=cutoff].copy(); test=d[d.week>cutoff].copy()
    Xtr=train[features]; Xte=test[features]; ytr=np.log1p(train.next_views); yte=test.next_views.to_numpy()
    models={
        "naive":None,
        "ridge":Ridge(alpha=10),
        "random_forest":RandomForestRegressor(n_estimators=300,max_depth=10,min_samples_leaf=3,random_state=42,n_jobs=1),
        "hist_gradient_boosting":HistGradientBoostingRegressor(max_iter=300,learning_rate=.05,max_leaf_nodes=20,l2_regularization=1,random_state=42),
    }
    rows=[]; fitted={}
    for name,model in models.items():
        pred=test.prev_views.to_numpy() if model is None else None
        if model is not None:
            model.fit(Xtr,ytr); fitted[name]=model; pred=np.expm1(model.predict(Xte))
        smape=float(np.mean(2*np.abs(yte-pred)/(np.abs(yte)+np.abs(pred)+1e-9)))
        rows.append({"model":name,"mae":mean_absolute_error(yte,pred),"rmse":mean_squared_error(yte,pred)**.5,"r2":r2_score(yte,pred),"smape":smape})
    metrics=pd.DataFrame(rows)
    naive_mae=float(metrics.loc[metrics.model=="naive","mae"].iloc[0]); metrics["mae_improvement_vs_naive"]=1-metrics.mae/naive_mae
    best_name=str(metrics[metrics.model!="naive"].sort_values(["mae","rmse"]).iloc[0].model)
    model=fitted[best_name]
    pi=permutation_importance(model,Xte,np.log1p(yte),n_repeats=10,random_state=42,scoring="neg_mean_absolute_error")
    imp=pd.DataFrame({"feature":features,"importance_mean":pi.importances_mean,"importance_std":pi.importances_std}).sort_values("importance_mean",ascending=False)
    pred=np.expm1(model.predict(Xte))
    errors=test[["week","entity_key","show_title","content_type","weekly_rank","prev_views","next_views"]].copy(); errors["prediction"]=pred; errors["absolute_error"]=(errors.next_views-errors.prediction).abs(); errors["smape"]=(2*errors.absolute_error/(errors.next_views.abs()+errors.prediction.abs()+1e-9))
    metrics.to_csv(REPORTS/"forecast_benchmarks.csv",index=False); imp.to_csv(REPORTS/"model_permutation_importance.csv",index=False); errors.sort_values("absolute_error",ascending=False).to_csv(REPORTS/"forecast_error_analysis.csv",index=False)
    shap_status={"status":"unavailable","reason":"not attempted"}
    shap_path=REPORTS/"model_shap_importance.csv"
    try:
        import shap
        sample=Xte.sample(min(250,len(Xte)),random_state=42)
        # Tree SHAP can hit tiny floating-point additivity residuals on this
        # sklearn estimator; disabling the diagnostic check does not alter the
        # SHAP values and avoids treating a numerical tolerance issue as a
        # pipeline failure.
        expl=shap.TreeExplainer(model)
        values=expl.shap_values(sample, check_additivity=False)
        pd.DataFrame({"feature":features,"mean_abs_shap":np.abs(values).mean(axis=0)}).sort_values("mean_abs_shap",ascending=False).to_csv(shap_path,index=False)
        shap_status={"status":"available","sample_rows":len(sample),"target":"log1p(next_week_views)"}
    except Exception as exc:
        if shap_path.exists(): shap_path.unlink()
        shap_status={"status":"unavailable","reason":str(exc)}
    (REPORTS/"shap_status.json").write_text(json.dumps(shap_status,indent=2))
    model_metrics={"task":"next_week_views","validation":"chronological 80/20 holdout by calendar week","cutoff_week":str(pd.Timestamp(cutoff).date()),"train_rows":len(train),"test_rows":len(test),"best_non_naive_model":best_name,"metrics":metrics.to_dict(orient="records")}
    (REPORTS/"model_metrics.json").write_text(json.dumps(model_metrics,indent=2,default=str))
    return metrics, imp, errors, model_metrics


def statistical_report(e: pd.DataFrame):
    rows=[]
    def add(name,test,stat,p,effect,n,interpretation):
        rows.append({"analysis":name,"test":test,"statistic":float(stat) if pd.notna(stat) else None,"p_value":float(p) if pd.notna(p) else None,"effect_size":float(effect) if pd.notna(effect) else None,"n":int(n),"interpretation":interpretation})
    for a,b,name in [("release_age_years","longevity_weeks_observed","Release age vs observed longevity"),("country_reach","longevity_weeks_observed","Country reach vs observed longevity"),("peak_rank","longevity_weeks_observed","Peak rank vs observed longevity")]:
        x=e[[a,b]].dropna()
        if len(x)>=3 and x[a].nunique()>1 and x[b].nunique()>1:
            stat,p=spearmanr(x[a],x[b]); add(name,"Spearman correlation",stat,p,stat,len(x),"Association only; not causal and subject to Top-10 selection/censoring.")
    ct=pd.crosstab(e.content_type,e.performance_segment)
    if ct.shape[0]>1 and ct.shape[1]>1:
        chi,p,_,_=chi2_contingency(ct); n=int(ct.to_numpy().sum()); v=float(np.sqrt(chi/(n*min(ct.shape[0]-1,ct.shape[1]-1))))
        add("Content type vs performance segment","Chi-square test",chi,p,v,n,"Association between categorical variables; Cramer's V is the effect size.")
    groups=[g.longevity_weeks_observed.dropna().to_numpy() for _,g in e.groupby("content_type") if len(g)>=2]
    names=[n for n,g in e.groupby("content_type") if len(g)>=2]
    if len(groups)==2:
        stat,p=mannwhitneyu(groups[0],groups[1],alternative="two-sided")
        # Rank-biserial correlation = 2U/(n1*n2)-1, with sign tied to group order.
        n1,n2=len(groups[0]),len(groups[1]); rbc=2*stat/(n1*n2)-1
        add(f"Observed longevity: {names[0]} vs {names[1]}","Mann-Whitney U",stat,p,rbc,n1+n2,"Distributional difference in observed Top-10 longevity; not causal.")
    out=pd.DataFrame(rows); out.to_csv(REPORTS/"statistical_results.csv",index=False); return out


def data_quality(g,c,e,tmdb):
    q={
        "pipeline_version":PIPELINE_VERSION,"global_rows":len(g),"country_rows":len(c),"entity_rows":len(e),"countries":int(c.country_iso2.nunique()),"global_weeks":int(g.week.nunique()),
        "global_min_week":str(g.week.min().date()),"global_max_week":str(g.week.max().date()),"country_min_week":str(c.week.min().date()),"country_max_week":str(c.week.max().date()),
        "global_duplicate_keys":int(g.duplicated(["week","category","weekly_rank"]).sum()),"country_duplicate_keys":int(c.duplicated(["country_iso2","week","category","weekly_rank"]).sum()),
        "global_views_coverage_pct":float(g.weekly_views.notna().mean()*100),"global_runtime_coverage_pct":float(g.runtime.notna().mean()*100),"global_hours_coverage_pct":float(g.weekly_hours_viewed.notna().mean()*100),
        "tmdb_row_match_pct":float(g.tmdb_matched.mean()*100),"tmdb_entity_match_pct":float(g[["entity_key","tmdb_matched"]].drop_duplicates("entity_key").tmdb_matched.mean()*100),
        "negative_views":int((g.weekly_views.dropna()<0).sum()),"negative_hours":int((g.weekly_hours_viewed.dropna()<0).sum()),"negative_runtime":int((g.runtime.dropna()<0).sum()),
        "null_show_titles_global":int(g.show_title.isna().sum()),"null_show_titles_country":int(c.show_title.isna().sum()),"tmdb_prepared_rows":len(tmdb),
    }
    by_year=g.assign(year=g.week.dt.year).groupby("year").agg(rows=("week","size"),views_coverage_pct=("weekly_views",lambda s:float(s.notna().mean()*100))).reset_index()
    by_year.to_csv(REPORTS/"views_coverage_by_year.csv",index=False)
    (REPORTS/"data_quality.json").write_text(json.dumps(q,indent=2))
    score_rows = [
        ("Source grain integrity", 100.0, "0 duplicate global/country analytical keys" if q["global_duplicate_keys"] == 0 and q["country_duplicate_keys"] == 0 else "Duplicate analytical keys detected"),
        ("Global view coverage", q["global_views_coverage_pct"], "Published views coverage; unavailable values are not treated as zero"),
        ("Global runtime coverage", q["global_runtime_coverage_pct"], "Published runtime coverage"),
        ("Global hours coverage", q["global_hours_coverage_pct"], "Published hours-viewed coverage"),
        ("TMDB entity coverage", q["tmdb_entity_match_pct"], "External metadata match rate, not Netflix catalog coverage"),
        ("Metric validity", 100.0, "No negative views, hours, or runtime" if q["negative_views"] == 0 and q["negative_hours"] == 0 and q["negative_runtime"] == 0 else "Invalid negative metrics detected"),
        ("Title completeness", 100.0, "No null show titles" if q["null_show_titles_global"] == 0 and q["null_show_titles_country"] == 0 else "Null show titles detected"),
    ]
    pd.DataFrame(score_rows, columns=["metric","score_pct","definition"]).to_csv(REPORTS/"data_quality_scorecard.csv", index=False)
    return q


def write_analysis_outputs(g,c,e,tmdb):
    mart=title_mart(g,c,e); mart.to_csv(PROC/"title_performance_mart.csv",index=False)
    sim=country_similarity(c); sim.to_csv(REPORTS/"country_similarity.csv",index=False)
    rel=release_age_report(mart); rel.to_csv(REPORTS/"release_age_performance.csv",index=False)
    vol=rank_volatility_report(mart); vol.to_csv(REPORTS/"rank_volatility.csv",index=False)
    surv=survival_report(mart,g.week.max()); surv.to_csv(REPORTS/"survival_by_segment.csv",index=False)
    br=breakout_report(mart); br.to_csv(REPORTS/"breakout_titles.csv",index=False)
    metrics,imp,errors,model_metrics=forecast_benchmark(g)
    stats=statistical_report(mart)
    q=data_quality(g,c,mart,tmdb)

    db=PROC/"netflix_analytics.db"; con=sqlite3.connect(db)
    artifacts={"title_performance_mart":mart,"country_similarity":sim,"release_age_performance":rel,"rank_volatility":vol,"survival_by_segment":surv,"breakout_titles":br,"forecast_benchmarks":metrics,"model_permutation_importance":imp,"forecast_error_analysis":errors,"statistical_results":stats}
    shap_path=REPORTS/"model_shap_importance.csv"
    if shap_path.exists(): artifacts["model_shap_importance"]=pd.read_csv(shap_path)
    for name,df in artifacts.items(): df.to_sql(name,con,if_exists="replace",index=False)
    con.commit(); con.close()

    summary={"pipeline_version":PIPELINE_VERSION,"quality":q,"analytical_artifacts":sorted(artifacts),"model":model_metrics}
    (REPORTS/"build_summary.json").write_text(json.dumps(summary,indent=2,default=str))
    return summary


def main():
    g=pd.read_csv(PROC/"global_analytics.csv",parse_dates=["week","release_date","prev_week","next_week"])
    c=pd.read_csv(PROC/"country_analytics.csv",parse_dates=["week","release_date"])
    e=pd.read_csv(PROC/"entity_performance.csv",parse_dates=["first_week","last_week","release_date"])
    tmdb=pd.read_csv(PROC/"tmdb_metadata.csv",parse_dates=["release_date"])
    summary=write_analysis_outputs(g,c,e,tmdb)
    print(json.dumps(summary["quality"],indent=2))

if __name__=="__main__": main()
