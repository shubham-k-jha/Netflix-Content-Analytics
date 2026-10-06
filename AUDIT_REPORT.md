# Final v8 Audit Report

## Scope

This release rebuilds the Netflix Top 10 intelligence project from the supplied current global/country TSVs, current Most Popular all-time ranking measured over the first 91 days, verified duplicate aliases, legacy TMDB reference metadata, and supplied H1 2026 engagement-report assets.

## Source validation

- Global weekly: 10,960 rows; 274 weeks; 2021-07-04 → 2026-09-27.
- Country weekly: 510,340 rows; 94 countries; 2021-07-04 → 2026-09-27.
- Current Most Popular: 40 rows.
- Global grain duplicates: 0.
- Country grain duplicates: 0.
- Negative views/hours/runtime: 0.
- Missing views/runtime are preserved as unavailable, never zero-filled.

## v8 additions audited

- Executive KPI layer.
- Title-level rank/views explorer.
- Entry, continuation, returning-title and churn/retention analysis.
- Entry cohorts and longevity curves.
- Global and country concentration metrics including HHI and Top-1/3/10 shares.
- Country drilldowns and title-market persistence.
- BH-FDR multiple-testing correction.
- Multi-cutoff chronological model stability.
- Data drift and model-performance drift reports.
- Catalog-ready optional ingestion with explicit provenance; no fabricated Netflix catalog.

## Code/data audit

- Clean source-driven rebuild completed.
- SQLite integrity: `PRAGMA integrity_check = ok`.
- SQLite tables: 30.
- SQL analyses: 25/25 passed.
- Automated tests: 35/35 passed.
- Python compilation: passed for source, dashboard, scripts and tests.
- The final package was re-extracted into a clean directory and the complete verification suite was run against that clean copy.
- Manifest contains 43 generated output files plus source/asset hashes.
- Randomized models use fixed seeds; Random Forest is single-threaded.

## Modeling audit

Forecast target: next-week views for entities with consecutive Top 10 observations. Validation is chronological by calendar week; no future rows are used for training.

Best non-naive model: hist_gradient_boosting.

- MAE: 752565
- RMSE: 1748407
- R²: 0.6898
- sMAPE: 0.1974

These are predictive performance metrics, not causal evidence.

## Catalog limitation

The supplied Netflix sources do not contain a complete current Netflix catalog. Public historical catalog snapshots exist, but treating one as a current authoritative Netflix catalog would be misleading. v8 therefore provides an optional `data/raw/netflix_titles.csv` ingestion contract and labels TMDB as external reference metadata.

## Dashboard environment

Dashboard source compilation passed. A live Streamlit HTTP smoke test depends on the declared Streamlit environment; it is not silently claimed as executed here.
