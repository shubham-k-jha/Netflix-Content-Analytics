# Methodology

## Source hierarchy

1. `all-weeks-global.tsv` is the canonical global weekly fact.
2. `all-weeks-countries.tsv` is the canonical country weekly fact.
3. `2026-10-05_global_alltime.tsv` is the canonical current Most Popular snapshot.
4. The other downloaded global TSVs are retained and verified as exact aliases; they are not counted twice.
5. The supplied TMDB CSV is optional external metadata.
6. The supplied H1 2026 PNGs are a visual report source and are transcribed into a small reference table.

## Missingness

Missing `weekly_views` and `runtime` are unavailable values, not zero. All view-based analyses explicitly restrict themselves to rows with published views.

## Entity definition

A cross-source `title_family_key` is a normalized Netflix title + content type + season/collection label where available. The global `entity_key` additionally includes the published global category so identical labels in different global categories are not silently collapsed. Country-level joins use `title_family_key` because the country source has only Films/TV categories.

## Forecasting

The predictive target is next-week views for entities already observed in consecutive Top 10 weeks. Features are restricted to information available before the target week. Validation uses a chronological 80/20 calendar-week holdout. A naive previous-week baseline is mandatory.

## Survival

Survival is measured at the entity level using elapsed calendar weeks from first to last observed week. A title whose last observation is before the dataset boundary is treated as an event; a title present at the final week is right-censored.

## Breakouts

Two-week view acceleration is calculated only when the current and two-prior observations are exactly 14 days apart and both view values are available. The breakout flag is the top 5% of valid accelerations in the observed sample.

## Statistical inference

Tests are descriptive/associational. They do not establish causality. Effect sizes are reported with p-values. The Top 10 selection mechanism and censoring limit causal interpretation.
