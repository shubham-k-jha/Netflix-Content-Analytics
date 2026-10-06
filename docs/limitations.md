# Limitations

- Netflix Top 10 data represents ranked titles, not the entire Netflix catalog.
- A title not appearing in Top 10 cannot be interpreted as zero viewing.
- Country rankings are audience geography, not production geography.
- Country data has no views/hours, so geographic analyses measure rank presence and breadth rather than country-level audience volume.
- Published weekly views/runtime begin later than the start of the Top 10 series; missingness is structural and preserved.
- The TMDB enrichment file is a legacy 2023 snapshot. It should not be interpreted as current metadata coverage.
- Survival results are subject to right-censoring and the possibility of re-entry before a title's final observed week.
- Forecasting predicts next-week views conditional on already being in consecutive Top 10 weeks; it is not a model of Top 10 entry or all-Netflix success.
- SHAP/permutation importance describes model behavior, not causal importance.
- The H1 2026 report assets are a separate semi-structured reference source, not a replacement for the weekly fact tables.
