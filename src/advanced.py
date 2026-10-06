"""v8 advanced analytics layer: executive KPIs, cohorts, retention/churn,
concentration, country drilldowns, statistical multiplicity control, model stability,
drift monitoring, and catalog/reference integration.

All catalog fields are explicitly classified as external reference data unless a
user-supplied Netflix catalog snapshot is placed at data/raw/netflix_titles.csv.
"""
from __future__ import annotations
import json, sqlite3
from pathlib import Path
import numpy as np
import pandas as pd
from scipy.stats import spearmanr, mannwhitneyu, chi2_contingency
from sklearn.ensemble import HistGradientBoostingRegressor, RandomForestRegressor
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from .config import ROOT, RAW, PROC, REPORTS, PIPELINE_VERSION


def bh_fdr(p):
    p=np.asarray(p,dtype=float); n=len(p)
    out=np.full(n,np.nan); valid=np.isfinite(p)
    if not valid.any(): return out
    idx=np.where(valid)[0]; order=idx[np.argsort(p[valid])]; ranked=p[order]
    q=ranked*n/np.arange(1,len(ranked)+1)
    q=np.minimum.accumulate(q[::-1])[::-1]
    out[order]=np.minimum(q,1.0)
    return out


def weekly_movement(g):
    x=g[['entity_key','show_title','content_type','week','weekly_rank']].copy()
    x=x.sort_values(['entity_key','week'])
    grp=x.groupby('entity_key',sort=False)
    x['prev_week']=grp.week.shift(1); x['prev_rank']=grp.weekly_rank.shift(1)
    x['is_continuing']=(x.week-x.prev_week).dt.days.eq(7)
    x['status']=np.select([
        x.prev_week.isna(), x.is_continuing & x.prev_rank.notna(), ~x.is_continuing & x.prev_week.notna()
    ],['new_entry','continuing','returning'],default='unknown')
    # Dropped titles are calculated by comparing each week's set to the next week's set.
    keys={w:set(z.entity_key) for w,z in x.groupby('week')}
    rows=[]
    weeks=sorted(keys)
    for w,nxt in zip(weeks,weeks[1:]):
        dropped=keys[w]-keys[nxt]
        rows.append({'week':w,'next_week':nxt,'new_entries':len(keys[nxt]-keys[w]),
                     'returning_entries':sum(1 for k in keys[nxt]-keys[w] if any(k in keys[ww] for ww in weeks[max(0,weeks.index(w)-51):weeks.index(w)])),
                     'continuing_titles':len(keys[w]&keys[nxt]),'dropped_titles':len(dropped),
                     'retention_rate':len(keys[w]&keys[nxt])/max(len(keys[w]),1),
                     'churn_rate':len(dropped)/max(len(keys[w]),1)})
    return pd.DataFrame(rows), x


def cohort_analysis(g):
    first=g.groupby('entity_key').week.min().rename('entry_week')
    e=g[['entity_key','show_title','content_type','week','weekly_views']].merge(first,left_on='entity_key',right_index=True)
    e['cohort_year']=e.entry_week.dt.year; e['age_weeks']=((e.week-e.entry_week).dt.days//7).astype(int)
    out=e.groupby(['cohort_year','age_weeks']).agg(entities=('entity_key','nunique'),
        mean_views=('weekly_views','mean'),median_views=('weekly_views','median')).reset_index()
    return out


def concentration(g,c):
    rows=[]
    for w, z in g.groupby('week'):
        v=z.weekly_views.dropna(); total=v.sum()
        shares=np.sort(v.to_numpy())[::-1]/total if total>0 else np.array([])
        hhi=float(np.sum(shares**2)) if len(shares) else np.nan
        rows.append({'week':w,'metric':'global_view_concentration','top1_share':shares[0] if len(shares)>0 else np.nan,
                     'top3_share':shares[:3].sum() if len(shares)>0 else np.nan,
                     'top10_share':shares[:10].sum() if len(shares)>0 else np.nan,'hhi':hhi,
                     'observations_with_views':len(v)})
    cc=[]
    for (w,cat),z in c.groupby(['week','category']):
        n=len(z); counts=z.country_iso2.value_counts(); shares=counts/n if n else pd.Series(dtype=float)
        cc.append({'week':w,'category':cat,'metric':'country_title_concentration','top1_share':shares.iloc[0] if len(shares) else np.nan,
                   'top3_share':shares.head(3).sum() if len(shares) else np.nan,'top10_share':shares.head(10).sum() if len(shares) else np.nan,
                   'hhi':float((shares**2).sum()) if len(shares) else np.nan,'observations_with_views':n})
    return pd.DataFrame(rows),pd.DataFrame(cc)


def country_drilldown(c):
    base=c.groupby(['country_iso2','country_name']).agg(
        appearances=('entity_key','size'),unique_entities=('entity_key','nunique'),weeks=('week','nunique'),
        avg_rank=('weekly_rank','mean')).reset_index()
    top=c.sort_values(['country_iso2','week','weekly_rank']).groupby(['country_iso2','show_title','content_type'],as_index=False).agg(
        appearances=('week','size'),best_rank=('weekly_rank','min'),weeks_present=('week','nunique'))
    top=top.sort_values(['country_iso2','appearances','best_rank'],ascending=[True,False,True])
    return base,top


def catalog_reference(tmdb,g):
    # This is an external metadata universe, not a claim of Netflix catalog membership.
    cols=[c for c in ['id','title','type','release_date','genres','production_countries','original_language','popularity','runtime'] if c in tmdb.columns]
    ref=tmdb[cols].drop_duplicates('id' if 'id' in cols else 'title').copy()
    hit=g[['title_key','content_type','show_title','entity_key']].drop_duplicates()
    ref['reference_source']='TMDB legacy metadata; external reference, not Netflix catalog'
    return ref, pd.DataFrame([{
        'catalog_source':'TMDB legacy metadata','classification':'external_reference_not_catalog','rows':len(ref),
        'note':'No authoritative Netflix-wide catalog snapshot was supplied; Top 10 membership is the authoritative Netflix performance universe.'
    }])


def netflix_catalog_if_supplied(g):
    p=RAW/'netflix_titles.csv'
    if not p.exists():
        return pd.DataFrame(), pd.DataFrame([{'status':'not_supplied','path':'data/raw/netflix_titles.csv','note':'Optional historical catalog snapshot. Not fabricated.'}])
    df=pd.read_csv(p,low_memory=False)
    required={'show_id','type','title','release_year'}
    missing=required-set(df.columns)
    if missing: raise ValueError(f'netflix_titles.csv missing required columns: {sorted(missing)}')
    df['catalog_source']='user_supplied_netflix_titles_snapshot'
    df['catalog_membership_claim']='snapshot_only'
    return df, pd.DataFrame([{'status':'loaded','path':'data/raw/netflix_titles.csv','rows':len(df),'note':'User-supplied snapshot; date/version must be documented by source owner.'}])


def catalog_performance_bridge(catalog,g):
    if catalog.empty: return pd.DataFrame()
    c=catalog.copy(); c['_title_key']=c.title.astype(str).str.strip().str.lower().str.replace(r'[^\\w]+',' ',regex=True).str.replace(r'\\s+',' ',regex=True).str.strip()
    c['_type']=np.where(c.type.astype(str).str.lower().str.contains('tv|show'),'TV','Film')
    hits=g[['title_key','content_type','entity_key','weekly_views','weekly_rank']].copy()
    hitagg=hits.groupby(['title_key','content_type']).agg(top10_entities=('entity_key','nunique'),peak_views=('weekly_views','max'),best_rank=('weekly_rank','min')).reset_index()
    return c.merge(hitagg,left_on=['_title_key','_type'],right_on=['title_key','content_type'],how='left')


def statistical_enhancement(stats):
    out=stats.copy(); out['q_value_bh_fdr']=bh_fdr(out.p_value.to_numpy()) if 'p_value' in out else np.nan
    out['significant_fdr_05']=out.q_value_bh_fdr<=0.05
    out.to_csv(REPORTS/'statistical_results.csv',index=False); return out


def forecast_model(name):
    if name=='ridge': return Ridge(alpha=10)
    if name=='random_forest': return RandomForestRegressor(n_estimators=100,max_depth=10,min_samples_leaf=3,random_state=42,n_jobs=1)
    return HistGradientBoostingRegressor(max_iter=300,learning_rate=.05,max_leaf_nodes=20,l2_regularization=1,random_state=42)


def model_stability(g):
    x=g[['entity_key','week','weekly_views','weekly_rank','cumulative_weeks_in_top_10']].copy().sort_values(['entity_key','week'])
    grp=x.groupby('entity_key',sort=False); x['prev_week']=grp.week.shift(1); x['prev_views']=grp.weekly_views.shift(1); x['prev_rank']=grp.weekly_rank.shift(1); x['next_week']=grp.week.shift(-1); x['next_views']=grp.weekly_views.shift(-1)
    x['cont_prev']=(x.week-x.prev_week).dt.days.eq(7); x['cont_next']=(x.next_week-x.week).dt.days.eq(7)
    d=x[(x.weekly_views.notna())&x.prev_views.notna()&x.next_views.notna()&x.cont_prev&x.cont_next].copy(); d['rank_change']=d.prev_rank-d.weekly_rank; d['wow']=d.weekly_views/d.prev_views.replace(0,np.nan)-1; d['log_prev']=np.log1p(d.prev_views); d=d.dropna()
    feats=['prev_views','weekly_rank','rank_change','cumulative_weeks_in_top_10','log_prev','wow']; weeks=sorted(d.week.unique()); cutpoints=[.7,.8,.9]; rows=[]
    for frac in cutpoints:
        cutoff=weeks[max(1,int(len(weeks)*frac))-1]; tr=d[d.week<=cutoff]; te=d[d.week>cutoff]
        if len(tr)<50 or len(te)<20: continue
        ytr=np.log1p(tr.next_views); yte=te.next_views.to_numpy(); Xtr=tr[feats]; Xte=te[feats]
        for name in ['ridge','random_forest','hist_gradient_boosting']:
            m=forecast_model(name); m.fit(Xtr,ytr); pred=np.expm1(m.predict(Xte))
            rows.append({'cutoff_fraction':frac,'cutoff_week':str(pd.Timestamp(cutoff).date()),'model':name,'train_rows':len(tr),'test_rows':len(te),
                         'mae':mean_absolute_error(yte,pred),'rmse':mean_squared_error(yte,pred)**.5,'r2':r2_score(yte,pred)})
    out=pd.DataFrame(rows); out.to_csv(REPORTS/'model_stability.csv',index=False); return out


def model_drift(g):
    x=g.copy(); x['year']=x.week.dt.year
    rows=[]
    for y,z in x.groupby('year'):
        views=z.weekly_views.dropna(); ranks=z.weekly_rank.dropna()
        rows.append({'period':str(y),'rows':len(z),'view_coverage_pct':z.weekly_views.notna().mean()*100,'median_views':views.median() if len(views) else np.nan,
                     'median_rank':ranks.median() if len(ranks) else np.nan,'median_runtime':z.runtime.median() if z.runtime.notna().any() else np.nan,'unique_entities':z.entity_key.nunique()})
    out=pd.DataFrame(rows); out.to_csv(REPORTS/'data_drift_by_year.csv',index=False)
    if len(out)>=2:
        base=out.iloc[0]; latest=out.iloc[-1]; drift=[]
        for col in ['median_views','median_rank','median_runtime','unique_entities']:
            a=float(base[col]); b=float(latest[col]); drift.append({'metric':col,'baseline_period':base.period,'latest_period':latest.period,'baseline':a,'latest':b,'relative_change':(b-a)/abs(a) if a else np.nan})
        pd.DataFrame(drift).to_csv(REPORTS/'data_drift_summary.csv',index=False)
    return out



def model_performance_drift():
    p=REPORTS/'forecast_error_analysis.csv'
    if not p.exists(): return pd.DataFrame()
    x=pd.read_csv(p,parse_dates=['week'])
    if x.empty: return x
    x['year']=x.week.dt.year
    out=x.groupby('year').agg(test_rows=('entity_key','size'),mae=('absolute_error','mean'),median_absolute_error=('absolute_error','median'),smape=('smape','mean'),median_actual_views=('next_views','median'),median_prediction=('prediction','median')).reset_index()
    out.to_csv(REPORTS/'model_performance_drift.csv',index=False)
    return out

def executive_kpis(g,c,mart,movement):
    latest=g.week.max(); cur=g[g.week.eq(latest)]; prev_week=latest-pd.Timedelta(days=7); prev=g[g.week.eq(prev_week)]
    views=cur.weekly_views.sum(min_count=1); prevv=prev.weekly_views.sum(min_count=1)
    return pd.DataFrame([{
        'latest_week':str(latest.date()),'titles_in_latest_week':cur.entity_key.nunique(),'published_view_total':views,
        'view_change_vs_prior_week_pct':(views/prevv-1) if pd.notna(views) and pd.notna(prevv) and prevv else np.nan,
        'new_entries':int(((cur.entity_key.isin(prev.entity_key)).eq(False)).sum()),
        'countries_active':c[c.week.eq(latest)].country_iso2.nunique(),'median_rank':cur.weekly_rank.median(),
        'breakout_candidates':int(mart.breakout_flag.sum()),'entities_total':len(mart),'avg_country_reach':mart.country_reach.mean()
    }])


def run_advanced(g,c,mart,tmdb,stats):
    outputs={}
    movement,detail=weekly_movement(g); movement.to_csv(REPORTS/'weekly_movement.csv',index=False); detail.to_csv(PROC/'entity_week_status.csv',index=False); outputs['weekly_movement']=movement
    cohort=cohort_analysis(g); cohort.to_csv(REPORTS/'cohort_analysis.csv',index=False); outputs['cohort_analysis']=cohort
    gc,cc=concentration(g,c); gc.to_csv(REPORTS/'global_concentration.csv',index=False); cc.to_csv(REPORTS/'country_concentration.csv',index=False); outputs['global_concentration']=gc; outputs['country_concentration']=cc
    cb,ct=country_drilldown(c); cb.to_csv(REPORTS/'country_drilldown.csv',index=False); ct.to_csv(REPORTS/'country_title_drilldown.csv',index=False); outputs['country_drilldown']=cb; outputs['country_title_drilldown']=ct
    stats=statistical_enhancement(stats); outputs['statistical_results']=stats
    stability=model_stability(g); outputs['model_stability']=stability
    drift=model_drift(g); outputs['data_drift_by_year']=drift
    mpd=model_performance_drift()
    if not mpd.empty: outputs['model_performance_drift']=mpd
    kpi=executive_kpis(g,c,mart,movement); kpi.to_csv(REPORTS/'executive_kpis.csv',index=False); outputs['executive_kpis']=kpi
    ref,refmeta=catalog_reference(tmdb,g); ref.to_csv(PROC/'external_catalog_reference.csv',index=False); refmeta.to_csv(REPORTS/'catalog_source_status.csv',index=False); outputs['external_catalog_reference']=ref
    catalog,catstatus=netflix_catalog_if_supplied(g); catstatus.to_csv(REPORTS/'netflix_catalog_status.csv',index=False)
    if not catalog.empty:
        catalog.to_csv(PROC/'netflix_catalog_snapshot.csv',index=False)
        bridge=catalog_performance_bridge(catalog,g); bridge.to_csv(REPORTS/'catalog_performance_bridge.csv',index=False); outputs['netflix_catalog_snapshot']=catalog; outputs['catalog_performance_bridge']=bridge
    db=PROC/'netflix_analytics.db'
    with sqlite3.connect(db) as con:
        for name,df in outputs.items(): df.to_sql(name,con,if_exists='replace',index=False)
        con.execute('CREATE INDEX IF NOT EXISTS idx_movement_week ON weekly_movement(week)')
        con.execute('CREATE INDEX IF NOT EXISTS idx_country_drilldown ON country_drilldown(country_iso2)')
    return outputs
