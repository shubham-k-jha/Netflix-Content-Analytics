from __future__ import annotations
import json, sqlite3
from pathlib import Path
import pandas as pd
import plotly.express as px
import streamlit as st

ROOT=Path(__file__).resolve().parents[1]; DB=ROOT/'data/processed/netflix_analytics.db'
st.set_page_config(page_title='Netflix Content Intelligence v8.1',layout='wide',initial_sidebar_state='expanded')

@st.cache_data(ttl=300)
def q(sql):
    with sqlite3.connect(DB) as con: return pd.read_sql_query(sql,con)

def qp(sql, params):
    with sqlite3.connect(DB) as con: return pd.read_sql_query(sql,con,params=params)

def metrics(items):
    cols=st.columns(len(items))
    for c,(a,b) in zip(cols,items): c.metric(a,b)

def fmt(v):
    if pd.isna(v): return '—'
    return f'{v:,.0f}' if abs(v)>=1000 else f'{v:.2f}'

st.title('Netflix Content Intelligence & Audience Performance — v8.1')
st.caption('Source-driven Top 10 intelligence • 274 weeks • 94 audience markets • 2021–2026')
pages=['Executive Overview','Weekly Briefing','Title Explorer','Global & Cohorts','Country Intelligence','Entry / Retention / Churn','Lifecycle & Concentration','Breakouts & Momentum','Forecasting & Model Stability','Statistical Evidence','Catalog & Metadata','Most Popular & H1 2026','Data Quality & Provenance']
page=st.sidebar.radio('Analysis',pages)

if page=='Executive Overview':
    k=q('SELECT * FROM executive_kpis LIMIT 1').iloc[0]
    metrics([('Latest week',k.latest_week),('Published views',fmt(k.published_view_total)),('WoW views',f'{k.view_change_vs_prior_week_pct:.1%}' if pd.notna(k.view_change_vs_prior_week_pct) else '—'),('Countries',fmt(k.countries_active)),('Breakouts',fmt(k.breakout_candidates)),('Entities',fmt(k.entities_total))])
    x=q('SELECT week,SUM(weekly_views) views FROM global_weekly WHERE weekly_views IS NOT NULL GROUP BY week ORDER BY week')
    st.plotly_chart(px.line(x,x='week',y='views',title='Published weekly global views'),use_container_width=True)
    st.subheader('Current week leaders')
    st.dataframe(q('SELECT show_title,content_type,weekly_rank,weekly_views,weekly_hours_viewed FROM global_weekly WHERE week=(SELECT MAX(week) FROM global_weekly) ORDER BY weekly_rank'),use_container_width=True)
    st.info('Top 10 data measures ranked Netflix audience performance, not the full Netflix catalog.')

elif page=='Weekly Briefing':
    k=q('SELECT * FROM executive_kpis LIMIT 1').iloc[0]
    st.subheader(f"Week ending {k.latest_week}")
    metrics([('New entries',fmt(k.new_entries)),('Countries active',fmt(k.countries_active)),('Breakout candidates',fmt(k.breakout_candidates)),('Entities observed',fmt(k.entities_total))])
    st.subheader('Current leaders')
    st.dataframe(q('SELECT show_title,content_type,season_title,category,weekly_rank,weekly_views,weekly_hours_viewed FROM global_weekly WHERE week=(SELECT MAX(week) FROM global_weekly) ORDER BY weekly_rank'),use_container_width=True)
    st.subheader('Largest weekly movements')
    mv=q('SELECT * FROM weekly_movement ORDER BY week DESC LIMIT 52')
    st.dataframe(mv,use_container_width=True)
    st.subheader('Breakouts')
    st.dataframe(q('SELECT show_title,content_type,category,peak_views,max_two_week_view_acceleration,breakout_flag FROM breakout_titles WHERE breakout_flag=1 ORDER BY max_two_week_view_acceleration DESC LIMIT 25'),use_container_width=True)

elif page=='Title Explorer':
    entities=q('SELECT entity_key,show_title,content_type,season_title,category FROM global_weekly GROUP BY entity_key,show_title,content_type,season_title,category ORDER BY show_title,content_type,season_title,category')
    labels=entities.apply(lambda r: f"{r.show_title} | {r.content_type} | {r.season_title or 'No season'} | {r.category}",axis=1)
    idx=st.selectbox('Content entity',range(len(entities)),format_func=lambda i: labels.iloc[i])
    entity=entities.iloc[idx]
    x=qp('SELECT week,weekly_rank,weekly_views,weekly_hours_viewed,cumulative_weeks_in_top_10,content_type,category,season_title FROM global_weekly WHERE entity_key=? ORDER BY week',(entity.entity_key,))
    metrics([('Weeks observed',len(x)),('Peak rank',x.weekly_rank.min()),('Peak views',x.weekly_views.max()),('Category',entity.category)])
    st.plotly_chart(px.line(x,x='week',y='weekly_rank',title='Rank history (1 is best)'),use_container_width=True)
    v=x.dropna(subset=['weekly_views'])
    if not v.empty: st.plotly_chart(px.line(v,x='week',y='weekly_views',title='Published views history'),use_container_width=True)
    st.download_button('Download entity CSV',x.to_csv(index=False),'title_entity.csv','text/csv')
    st.dataframe(x,use_container_width=True)

elif page=='Global & Cohorts':
    x=q('SELECT week,category,SUM(weekly_views) views,SUM(weekly_hours_viewed) hours FROM global_weekly WHERE weekly_views IS NOT NULL GROUP BY week,category ORDER BY week')
    st.plotly_chart(px.line(x,x='week',y='views',color='category',title='Weekly global views by category'),use_container_width=True)
    c=q('SELECT * FROM cohort_analysis')
    st.subheader('Entry cohorts')
    st.plotly_chart(px.line(c[c.age_weeks<=20],x='age_weeks',y='median_views',color='cohort_year',title='Median published views by weeks since Top-10 entry'),use_container_width=True)
    st.dataframe(c,use_container_width=True)

elif page=='Country Intelligence':
    countries=q('SELECT country_iso2,country_name FROM country_drilldown ORDER BY country_name')
    country=st.selectbox('Audience market',countries.country_name.tolist())
    code=countries.loc[countries.country_name==country,'country_iso2'].iloc[0]
    base=qp('SELECT * FROM country_drilldown WHERE country_iso2=?',(code,))
    top=qp('SELECT * FROM country_title_drilldown WHERE country_iso2=? ORDER BY appearances DESC,best_rank LIMIT 50',(code,))
    metrics([('Appearances',fmt(base.appearances.iloc[0])),('Unique titles',fmt(base.unique_entities.iloc[0])),('Weeks',fmt(base.weeks.iloc[0])),('Avg rank',f"{base.avg_rank.iloc[0]:.2f}")])
    st.dataframe(top,use_container_width=True)
    st.subheader('Cross-market similarity')
    sim=q('SELECT * FROM country_similarity ORDER BY jaccard_similarity DESC LIMIT 100'); st.dataframe(sim,use_container_width=True); st.download_button('Download country analysis',top.to_csv(index=False),'country_titles.csv','text/csv')
    st.caption('Country means audience market, not production country.')

elif page=='Entry / Retention / Churn':
    x=q('SELECT * FROM weekly_movement ORDER BY week')
    st.plotly_chart(px.line(x,x='week',y=['retention_rate','churn_rate'],title='Weekly retention and churn'),use_container_width=True)
    st.plotly_chart(px.bar(x.tail(52),x='week',y=['new_entries','returning_entries','continuing_titles'],title='Latest 52 weeks: entry/return/continuation'),use_container_width=True)
    st.dataframe(x.tail(104),use_container_width=True)

elif page=='Lifecycle & Concentration':
    s=q('SELECT * FROM survival_by_segment ORDER BY segment_type,segment,duration_week')
    st.plotly_chart(px.line(s,x='duration_week',y='survival_probability',color='segment',facet_row='segment_type',title='Observed Top-10 survival with right-censoring'),use_container_width=True)
    g=q('SELECT * FROM global_concentration')
    st.plotly_chart(px.line(g,x='week',y=['top1_share','top3_share','top10_share'],title='Global view concentration'),use_container_width=True)
    st.dataframe(q('SELECT * FROM country_concentration ORDER BY week DESC LIMIT 200'),use_container_width=True)

elif page=='Breakouts & Momentum':
    st.dataframe(q('SELECT * FROM breakout_titles ORDER BY max_two_week_view_acceleration DESC LIMIT 150'),use_container_width=True)
    st.dataframe(q('SELECT * FROM rank_volatility ORDER BY rank_volatility_index DESC LIMIT 150'),use_container_width=True)

elif page=='Forecasting & Model Stability':
    m=q('SELECT * FROM forecast_benchmarks ORDER BY mae'); st.dataframe(m,use_container_width=True)
    st.plotly_chart(px.bar(m,x='model',y='mae',title='Chronological holdout MAE'),use_container_width=True)
    st.subheader('Stability across chronological cut points')
    s=q('SELECT * FROM model_stability'); st.plotly_chart(px.line(s,x='cutoff_fraction',y='mae',color='model',markers=True,title='MAE stability'),use_container_width=True); st.dataframe(s,use_container_width=True)
    st.subheader('Permutation importance'); st.dataframe(q('SELECT * FROM model_permutation_importance ORDER BY importance_mean DESC'),use_container_width=True)
    st.subheader('Forecast error'); st.dataframe(q('SELECT * FROM forecast_error_analysis ORDER BY absolute_error DESC LIMIT 100'),use_container_width=True)
    shap=ROOT/'reports/model_shap_importance.csv'
    if shap.exists(): st.subheader('SHAP'); st.dataframe(pd.read_csv(shap),use_container_width=True)

elif page=='Statistical Evidence':
    d=q('SELECT * FROM statistical_results ORDER BY q_value_bh_fdr,p_value'); st.dataframe(d,use_container_width=True)
    st.caption('BH-FDR q-values control expected false-discovery rate across the reported tests. Associations are not causal.')

elif page=='Catalog & Metadata':
    st.subheader('Catalog-source status')
    st.dataframe(q('SELECT * FROM catalog_source_status'),use_container_width=True)
    st.dataframe(q('SELECT * FROM netflix_catalog_status'),use_container_width=True)
    st.subheader('External metadata reference')
    st.dataframe(q('SELECT * FROM external_catalog_reference LIMIT 500'),use_container_width=True)
    st.caption('TMDB metadata is external reference data and must not be interpreted as a complete or current Netflix catalog.')
    bridge=ROOT/'reports/catalog_performance_bridge.csv'
    if bridge.exists(): st.subheader('Catalog ↔ Top 10 bridge'); st.dataframe(pd.read_csv(bridge),use_container_width=True)

elif page=='Most Popular & H1 2026':
    st.dataframe(q('SELECT * FROM most_popular ORDER BY content_type,rank'),use_container_width=True)
    st.subheader('H1 2026 engagement report reference'); st.dataframe(q('SELECT * FROM h1_2026_most_watched ORDER BY content_type,rank'),use_container_width=True)
    for fn in ['NFLX_H12026_EngagementReport_Top10Movies.png','NFLX_H12026_EngagementReport_Top10Shows.png']:
        p=ROOT/'assets'/fn
        if p.exists(): st.image(str(p),caption=fn,use_container_width=True)

else:
    dq=json.loads((ROOT/'reports/data_quality.json').read_text()); st.json(dq); cov=ROOT/'reports/data_quality_scorecard.csv';
    if cov.exists(): st.subheader('Data-quality scorecard'); st.dataframe(pd.read_csv(cov),use_container_width=True)
    st.subheader('Data drift'); st.dataframe(q('SELECT * FROM data_drift_by_year'),use_container_width=True)
    con=sqlite3.connect(DB)
    has_mpd=bool(con.execute("SELECT 1 FROM sqlite_master WHERE type='table' AND name='model_performance_drift'").fetchone())
    con.close()
    if has_mpd: st.subheader('Model performance drift'); st.dataframe(q('SELECT * FROM model_performance_drift'),use_container_width=True)
    if (ROOT/'reports/data_drift_summary.csv').exists(): st.dataframe(pd.read_csv(ROOT/'reports/data_drift_summary.csv'),use_container_width=True)
    st.subheader('Source registry'); sr=q('SELECT * FROM source_registry ORDER BY source_key'); st.dataframe(sr,use_container_width=True); st.download_button('Download source registry',sr.to_csv(index=False),'source_registry.csv','text/csv')
    st.json(json.loads((ROOT/'reports/build_summary.json').read_text()))
