from __future__ import annotations
import json, sqlite3, py_compile
from pathlib import Path
import pandas as pd

ROOT=Path(__file__).resolve().parents[1]


def test_source_files_exist():
    required=['all-weeks-global.tsv','all-weeks-countries.tsv','2026-10-05_global_weekly.tsv','2026-10-05_global_alltime.tsv','most-popular_global_weekly.tsv','most-popular_global_alltime.tsv','tmdb_data_legacy_2023.csv']
    assert all((ROOT/'data/raw'/x).exists() for x in required)


def test_current_global_shape_and_range():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    assert len(df)==10960
    assert df.week.min()=='2021-07-04' and df.week.max()=='2026-09-27'
    assert df.week.nunique()==274
    assert df.weekly_rank.min()==1 and df.weekly_rank.max()==10



def test_global_entity_week_is_unique_after_category_disambiguation():
    df=pd.read_csv(ROOT/'data/processed/global_analytics.csv')
    assert df.duplicated(['entity_key','week']).sum()==0


def test_global_week_structure_is_exact():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    assert (df.groupby('week').size()==40).all()
    assert (df.groupby(['week','category']).size()==10).all()


def test_current_country_shape_and_range():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-countries.tsv',sep='\t')
    assert len(df)==510340
    assert df.country_iso2.nunique()==94
    assert df.week.min()=='2021-07-04' and df.week.max()=='2026-09-27'


def test_global_grain_unique():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    assert df.duplicated(['week','category','weekly_rank']).sum()==0


def test_country_grain_unique():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-countries.tsv',sep='\t')
    assert df.duplicated(['country_iso2','week','category','weekly_rank']).sum()==0


def test_alias_files_exact():
    a=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    for name in ['2026-10-05_global_weekly.tsv','most-popular_global_weekly.tsv']:
        b=pd.read_csv(ROOT/'data/raw'/name,sep='\t'); assert a.equals(b)
    a=pd.read_csv(ROOT/'data/raw/2026-10-05_global_alltime.tsv',sep='\t')
    b=pd.read_csv(ROOT/'data/raw/most-popular_global_alltime.tsv',sep='\t'); assert a.equals(b)


def test_alltime_contract():
    df=pd.read_csv(ROOT/'data/raw/2026-10-05_global_alltime.tsv',sep='\t')
    assert len(df)==40 and df.duplicated(['category','rank']).sum()==0
    assert df['rank'].min()==1 and df['rank'].max()==10


def test_views_coverage_is_missing_not_zero():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    assert df.weekly_views.isna().sum()>0
    assert (df.weekly_views.dropna()>=0).all()


def test_no_negative_source_metrics():
    df=pd.read_csv(ROOT/'data/raw/all-weeks-global.tsv',sep='\t')
    for c in ['weekly_views','weekly_hours_viewed','runtime']:
        assert (df[c].dropna()>=0).all()


def test_h1_asset_files_exist():
    assert (ROOT/'assets/NFLX_H12026_EngagementReport_Top10Movies.png').exists()
    assert (ROOT/'assets/NFLX_H12026_EngagementReport_Top10Shows.png').exists()


def test_processed_artifacts_exist():
    for p in ['global_analytics.csv','country_analytics.csv','most_popular.csv','tmdb_metadata.csv','entity_performance.csv','title_performance_mart.csv','netflix_analytics.db']:
        assert (ROOT/'data/processed'/p).exists()


def test_processed_row_counts():
    assert len(pd.read_csv(ROOT/'data/processed/global_analytics.csv'))==10960
    assert len(pd.read_csv(ROOT/'data/processed/country_analytics.csv'))==510340
    assert len(pd.read_csv(ROOT/'data/processed/most_popular.csv'))==40


def test_title_mart_contract():
    df=pd.read_csv(ROOT/'data/processed/title_performance_mart.csv')
    required={'entity_key','rank_volatility_index','country_diversity_index','performance_segment','breakout_flag','views_coverage_weeks','elapsed_weeks'}
    assert required.issubset(df.columns) and len(df)>0 and df.entity_key.is_unique


def test_missing_view_sums_are_not_zero_for_all_missing_entities():
    g=pd.read_csv(ROOT/'data/processed/global_analytics.csv')
    e=pd.read_csv(ROOT/'data/processed/entity_performance.csv')
    all_missing=g.groupby('entity_key').weekly_views.apply(lambda s:s.notna().sum()==0)
    check=e.set_index('entity_key').loc[all_missing[all_missing].index,'total_views']
    assert check.isna().all()


def test_country_similarity_bounds():
    d=pd.read_csv(ROOT/'reports/country_similarity.csv')
    assert ((d.jaccard_similarity>=0)&(d.jaccard_similarity<=1)).all()


def test_survival_bounds():
    d=pd.read_csv(ROOT/'reports/survival_by_segment.csv')
    assert {'segment_type','segment','duration_week','survival_probability'}.issubset(d.columns)
    assert ((d.survival_probability>=0)&(d.survival_probability<=1)).all()


def test_forecast_models_present():
    d=pd.read_csv(ROOT/'reports/forecast_benchmarks.csv')
    assert {'naive','ridge','random_forest','hist_gradient_boosting'}.issubset(set(d.model))
    assert (d.mae>=0).all()


def test_forecast_is_chronological():
    m=json.loads((ROOT/'reports/model_metrics.json').read_text())
    assert 'chronological' in m['validation'].lower()
    assert m['train_rows']>0 and m['test_rows']>0


def test_breakout_contract():
    d=pd.read_csv(ROOT/'reports/breakout_titles.csv')
    assert 'max_two_week_view_acceleration' in d.columns
    assert d.breakout_flag.isin([True,False,0,1]).all()


def test_statistics_contract():
    d=pd.read_csv(ROOT/'reports/statistical_results.csv')
    assert {'analysis','test','p_value','effect_size','n'}.issubset(d.columns)
    assert (d.n>=2).all()


def test_h1_table():
    d=pd.read_csv(ROOT/'data/processed/h1_2026_most_watched.csv')
    assert len(d)==20 and set(d.content_type)=={'Film','TV'}
    assert d.groupby('content_type')['rank'].nunique().to_dict()=={'Film':10,'TV':10}


def test_sql_execution():
    r=json.loads((ROOT/'reports/sql_execution_report.json').read_text())
    assert r['sql_files']==25 and r['passed']==25


def test_sqlite_tables():
    con=sqlite3.connect(ROOT/'data/processed/netflix_analytics.db')
    names={x[0] for x in con.execute("select name from sqlite_master where type='table'")}; con.close()
    expected={'global_weekly','country_weekly','most_popular','tmdb_metadata','entity_performance','survival_curve','h1_2026_most_watched','source_registry','title_performance_mart','country_similarity','release_age_performance','rank_volatility','survival_by_segment','breakout_titles','forecast_benchmarks','model_permutation_importance','forecast_error_analysis','statistical_results'}
    assert expected.issubset(names)



def test_source_alias_validation():
    d=json.loads((ROOT/'reports/source_alias_validation.json').read_text())
    assert d['counts_as_unique_facts']['global_weekly_aliases'] is False
    assert d['counts_as_unique_facts']['alltime_aliases'] is False
    assert d['h1_2026_archive_preserved'] is True


def test_manifest_contract():
    m=json.loads((ROOT/'reports/pipeline_run_manifest.json').read_text())
    assert m['pipeline_version']=='8.1.0' and m['deterministic_build'] is True
    assert 'data/raw/all-weeks-global.tsv' in m['source_files']
    assert 'assets/NFLX_H12026_EngagementReport_Top10Movies.png' in m['asset_files']


def test_data_quality_zero_errors():
    q=json.loads((ROOT/'reports/data_quality.json').read_text())
    for k in ['global_duplicate_keys','country_duplicate_keys','negative_views','negative_hours','negative_runtime','null_show_titles_global','null_show_titles_country']:
        assert q[k]==0


def test_schema_contract():
    c=json.loads((ROOT/'docs/schema_contract.json').read_text())
    assert c['version']=='8.1.0'
    assert 'global_weekly' in c['required_tables']


def test_python_sources_compile():
    for p in list((ROOT/'src').glob('*.py'))+list((ROOT/'scripts').glob('*.py'))+list((ROOT/'tests').glob('*.py'))+[ROOT/'dashboard/app.py']:
        py_compile.compile(str(p),doraise=True)


def test_v8_advanced_artifacts():
    required=['weekly_movement.csv','cohort_analysis.csv','global_concentration.csv','country_concentration.csv','country_drilldown.csv','country_title_drilldown.csv','model_stability.csv','data_drift_by_year.csv','model_performance_drift.csv','executive_kpis.csv','catalog_source_status.csv','netflix_catalog_status.csv']
    assert all((ROOT/'reports'/x).exists() for x in required)

def test_v8_sql_tables():
    con=sqlite3.connect(ROOT/'data/processed/netflix_analytics.db')
    names={x[0] for x in con.execute("select name from sqlite_master where type='table'")}
    con.close()
    expected={'weekly_movement','cohort_analysis','global_concentration','country_concentration','country_drilldown','country_title_drilldown','model_stability','data_drift_by_year','model_performance_drift','executive_kpis','external_catalog_reference','statistical_results'}
    assert expected.issubset(names)

def test_v8_fdr_columns():
    d=pd.read_csv(ROOT/'reports/statistical_results.csv')
    assert {'q_value_bh_fdr','significant_fdr_05'}.issubset(d.columns)
    assert ((d.q_value_bh_fdr.dropna()>=0)&(d.q_value_bh_fdr.dropna()<=1)).all()

def test_v8_catalog_is_explicitly_external_when_no_catalog_supplied():
    d=pd.read_csv(ROOT/'reports/catalog_source_status.csv')
    assert 'external_reference_not_catalog' in set(d.classification)

def test_v8_manifest_contains_advanced_outputs():
    m=json.loads((ROOT/'reports/pipeline_run_manifest.json').read_text())
    assert m['pipeline_version']=='8.1.0'
    assert 'reports/model_stability.csv' in m['output_files']


def test_v81_quality_scorecard_and_dashboard_contract():
    score = pd.read_csv(ROOT/'reports/data_quality_scorecard.csv')
    assert {'metric','score_pct','definition'}.issubset(score.columns)
    assert len(score) >= 7
    app=(ROOT/'dashboard/app.py').read_text()
    assert "Weekly Briefing" in app
    assert "Download entity CSV" in app
    assert "Content entity" in app
    assert "data_quality_scorecard.csv" in app

def test_v81_root_and_no_stale_v7_paths():
    assert ROOT.name == 'netflix_v8_1'
    text='\n'.join(str(p) for p in ROOT.rglob('*') if p.is_file())
    assert 'netflix_v7' not in text
