::: {align="center"}
# Netflix Content Intelligence

**Global & Country Analytics · Content Lifecycle · Statistical Evidence
· Forecasting · Machine Learning**

```{=html}
<p>
```
`<img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Version-8.1-E50914?style=flat-square" alt="Version 8.1">`{=html}
`<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/SQL-25%20Analyses-336791?style=flat-square" alt="SQL analyses">`{=html}
`<img src="https://img.shields.io/badge/Tests-37%2F37%20Passing-2EA44F?style=flat-square" alt="Automated tests">`{=html}
`<img src="https://img.shields.io/badge/Markets-94-111827?style=flat-square" alt="Audience markets">`{=html}
```{=html}
</p>
```
**A reproducible analytics system built from Netflix's published Top 10
data.**

[Data Sources](#-official-data-sources) · [Visual
Gallery](#-visual-gallery) · [Forecast Benchmark](#-forecast-benchmark)
· [Architecture](#-architecture) · [Get Started](#-get-started)
:::

------------------------------------------------------------------------

## Project at a glance

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}10,960`</strong>`{=html}`<br>`{=html}Global weekly
observations
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}510,340`</strong>`{=html}`<br>`{=html}Country weekly
observations
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}94`</strong>`{=html}`<br>`{=html}Audience markets
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}274 weeks`</strong>`{=html}`<br>`{=html}2021-07-04 →
2026-09-27
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td align="center">
```
`<strong>`{=html}25 / 25`</strong>`{=html}`<br>`{=html}SQL analyses
passed
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}37 / 37`</strong>`{=html}`<br>`{=html}Automated tests
passed
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}64 / 64`</strong>`{=html}`<br>`{=html}Manifest hashes
matched
```{=html}
</td>
```
```{=html}
<td align="center">
```
`<strong>`{=html}13 pages`</strong>`{=html}`<br>`{=html}Streamlit
dashboard
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
> **Measurement boundary:** this project analyzes Netflix's published
> Top 10 measurements. It does not measure total viewing across the
> entire Netflix catalog. A title absent from the Top 10 is not
> equivalent to zero viewing.

## What this project does

Netflix Content Intelligence combines data ingestion, validation,
normalization, SQL analytics, statistical testing, lifecycle
measurement, market comparisons, forecasting, model diagnostics, and an
interactive dashboard.

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
**BUSINESS & MARKET INTELLIGENCE**

-   Global weekly performance and rank trends
-   Country-level audience-market comparisons
-   Title retention, returns, and drop-off
-   Cohorts, survival, and right-censoring
-   Concentration and market breadth
-   Breakout detection and two-week momentum

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
**ANALYTICS ENGINEERING & MODELING**

-   Source contracts and data-quality validation
-   25 executable SQL analysis modules
-   Effect sizes, hypothesis tests, and FDR control
-   Chronological next-week views forecasting
-   Permutation importance and SHAP when available
-   Provenance manifests, hashes, tests, and SQLite

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## Horizontal infographic · From source to insight

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}01`</strong>`{=html}`<br>`{=html}📥`<br>`{=html}**INGEST**`<br>`{=html}`<sub>`{=html}Official
Netflix TSVs`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}02`</strong>`{=html}`<br>`{=html}🧹`<br>`{=html}**VALIDATE**`<br>`{=html}`<sub>`{=html}Schema
· grain · quality`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}03`</strong>`{=html}`<br>`{=html}🧱`<br>`{=html}**MODEL**`<br>`{=html}`<sub>`{=html}Normalized
data marts`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}04`</strong>`{=html}`<br>`{=html}🔎`<br>`{=html}**ANALYZE**`<br>`{=html}`<sub>`{=html}SQL
· statistics · lifecycle`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}05`</strong>`{=html}`<br>`{=html}🤖`<br>`{=html}**FORECAST**`<br>`{=html}`<sub>`{=html}Time-aware
ML evaluation`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="16%">
```
`<strong>`{=html}06`</strong>`{=html}`<br>`{=html}📊`<br>`{=html}**DELIVER**`<br>`{=html}`<sub>`{=html}Dashboard
· reports · tests`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## Horizontal infographic · Project footprint

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="20%">
```
`<strong>`{=html}10,960`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Global
records`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="20%">
```
`<strong>`{=html}510,340`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Country
records`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="20%">
```
`<strong>`{=html}94`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Markets`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="20%">
```
`<strong>`{=html}25`</strong>`{=html}`<br>`{=html}`<sub>`{=html}SQL
modules`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="20%">
```
`<strong>`{=html}37`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Automated
tests`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
*These figures are reported by the supplied project audit; they are not
represented as freshly re-run in this README update.*

## Visual gallery

The visuals follow the analytical story: system design and scale,
performance, lifecycle and market behavior, then model evaluation and
data quality. Netflix H1 2026 report images are contextual references
and remain separate from the weekly Top 10 facts.

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
### 1 · System architecture

`<img src="assets/02_architecture.png" alt="System architecture" width="100%">`{=html}

The pipeline from official sources through validation, analytics,
modeling, and reporting.

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
### 2 · Project scale

`<img src="assets/03_project_kpis.png" alt="Project KPIs" width="100%">`{=html}

Dataset size, market coverage, SQL modules, and automated tests.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 3 · Global weekly performance

`<img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="100%">`{=html}

Observed global Top 10 viewing activity over time.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 4 · Country-market coverage

`<img src="assets/05_country_coverage.png" alt="Country-market coverage" width="100%">`{=html}

Geographic breadth of audience-market observations---not production
countries.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 5 · Retention and churn

`<img src="assets/08_retention_churn.png" alt="Retention and churn" width="100%">`{=html}

Continuation, disappearance, and return across weekly observations.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 6 · Global concentration

`<img src="assets/09_global_concentration.png" alt="Global concentration" width="100%">`{=html}

Whether observed performance is broadly distributed or concentrated.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 7 · Breakout titles

`<img src="assets/10_breakout_titles.png" alt="Breakout titles" width="100%">`{=html}

Titles with unusual short-term acceleration under the project framework.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 8 · Country similarity

`<img src="assets/11_country_similarity.png" alt="Country similarity" width="100%">`{=html}

Market similarities based on observed title-performance patterns.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 9 · Statistical effects

`<img src="assets/12_statistical_effects.png" alt="Statistical effects" width="100%">`{=html}

Hypothesis-test evidence and effect sizes, with multiple-testing control
where applicable.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 10 · Forecast benchmark

`<img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="100%">`{=html}

Chronological holdout results versus a naive baseline.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 11 · Feature importance

`<img src="assets/13_model_feature_importance.png" alt="Forecast feature importance" width="100%">`{=html}

Predictors contributing to forecast performance; importance is not
causality.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 12 · Model stability

`<img src="assets/14_model_stability.png" alt="Model stability" width="100%">`{=html}

Variation in model behavior and errors across time or validation slices.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 13 · Data coverage drift

`<img src="assets/15_data_drift.png" alt="Data coverage drift" width="100%">`{=html}

Coverage changes that may affect interpretation of apparent trends.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 14 · Cohort lifecycle

`<img src="assets/16_cohort_median_views.png" alt="Cohort lifecycle" width="100%">`{=html}

Median observed views across lifecycle positions for title cohorts.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 15 · Data quality

`<img src="assets/07_data_quality.png" alt="Data quality scorecard" width="100%">`{=html}

Source grain, metric validity, coverage, title completeness, and
metadata coverage.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
### 16 · H1 2026: Top Movies

`<img src="assets/NFLX_H12026_EngagementReport_Top10Movies.png" alt="Netflix H1 2026 top movies" width="100%">`{=html}

Official Netflix reference visual, separate from weekly Top 10 data.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
<tr>
```
```{=html}
<td valign="top">
```
### 17 · H1 2026: Top Shows

`<img src="assets/NFLX_H12026_EngagementReport_Top10Shows.png" alt="Netflix H1 2026 top shows" width="100%">`{=html}

Separate company-level reference, not a weekly Top 10 fact table.

```{=html}
</td>
```
```{=html}
<td valign="top">
```
**How to read the story:** sources → scale → performance → lifecycle and
markets → statistical evidence → forecasting → stability and quality.

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```

------------------------------------------------------------------------

## Official data sources

  ---------------------------------------------------------------------------------------------------------------------
  Source                                                                            Role
  --------------------------------------------------------------------------------- -----------------------------------
  [Global Weekly Top 10                                                             Global weekly title performance
  TSV](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv)               

  [Country Weekly Top 10                                                            Weekly performance by audience
  TSV](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv)            market

  [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular)          Separate first-91-days ranking

  [Netflix Top 10 portal](https://www.netflix.com/tudum/top10)                      Published interface and methodology
                                                                                    context

  [What We Watched --- H1                                                           Separate engagement-report
  2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026)   reference
  ---------------------------------------------------------------------------------------------------------------------

Optional TMDB data is external reference metadata---not an authoritative
Netflix-wide catalog or Netflix audience-performance data.

### Audited data scope

  Measure                                                  Reported result
  ------------------------------ -----------------------------------------
  Global weekly observations                                        10,960
  Country weekly observations                                      510,340
  Audience markets                                                      94
  Weekly coverage                                                274 weeks
  Coverage period                                 2021-07-04 to 2026-09-27
  Current Most Popular records                                          40
  Global source grain                                     40 rows per week
  Country source grain             10 rows per category, week, and country

## Architecture

``` text
Official Netflix sources
        │
        ▼
Raw TSV / CSV ingestion
        │
        ▼
Validation: schema · grain · dates · duplicates · missingness · metric checks
        │
        ▼
Normalization: dates · entity keys · categories · content type
        │
        ▼
Analytical marts + SQLite
        │
        ├───────────────────────┐
        ▼                       ▼
   SQL analytics          Statistical analysis
        └───────────┬───────────┘
                    ▼
Lifecycle · Survival · Concentration · Market similarity · Breakouts
                    │
                    ▼
Chronological forecasting · Model interpretation · Stability / drift
                    │
                    ▼
Reports · CSV exports · Streamlit dashboard
```

## Analytical framework

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
**PERFORMANCE** - Peak and average rank - Peak views and hours -
Observed and elapsed longevity - Rank volatility and performance
segments

**LIFECYCLE & SURVIVAL** - New, continuing, returning, and dropped
titles - Entry cohorts and weeks since entry - Retention and survival
curves - Right-censoring at the observation boundary

**MARKET INTELLIGENCE** - Country reach and title-market persistence -
Jaccard similarity between markets - Top-1, Top-3, and Top-10
concentration - Herfindahl--Hirschman Index (HHI) -
Global-versus-country comparisons

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
**MOMENTUM & BREAKOUTS** - Week-over-week movement and rank changes -
Two-week view acceleration - New entries and cross-market expansion

**STATISTICAL EVIDENCE** - Distribution and group comparisons -
Association analysis and effect sizes - Hypothesis tests and p-values -
Benjamini--Hochberg false discovery rate control

**PREDICTIVE ANALYTICS** - Naive baseline, Ridge, Random Forest,
HistGradientBoosting - Forecast error and chronological stability -
Permutation importance and SHAP when available

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## Forecasting and machine learning

### Prediction task

> **Estimate next-week views for entities with consecutive Top 10
> observations.**

This is not a model for predicting whether any arbitrary title will
enter the Top 10. The current task focuses on entities already observed
in consecutive weeks.

### Chronological validation

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="33%">
```
`<strong>`{=html}80 /
20`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Chronological
holdout`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
`<strong>`{=html}2026-01-25`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Cutoff
week`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="33%">
```
`<strong>`{=html}1,690 /
394`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Train / test
rows`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
The split preserves time order to reduce temporal leakage. Randomly
mixing future observations into training would undermine this
evaluation.

### Forecast benchmark

  ------------------------------------------------------------------------------------------------------
  Model                                   MAE               RMSE           R²        sMAPE           MAE
                                                                                             improvement
                                                                                               vs. naive
  -------------------------- ---------------- ------------------ ------------ ------------ -------------
  Naive                          4,818,781.73       7,693,942.50      -5.0073       0.7051            0%

  Ridge                          1,306,746.39       2,481,223.14       0.3752       0.3047        72.88%

  Random Forest                    772,008.52       1,811,793.36       0.6669       0.2018        83.98%

  **HistGradientBoosting**     **752,565.16**   **1,748,406.59**   **0.6898**   **0.1974**    **84.38%**
  ------------------------------------------------------------------------------------------------------

The supplied audit identifies HistGradientBoosting as the strongest
non-naive model on this holdout, with an **84.38% MAE improvement over
the naive baseline**. These values describe this defined task and split;
they are not evidence of causation or a guarantee of future performance.

### Model diagnostics

-   Feature and permutation importance
-   SHAP explanations when available
-   Error distributions and metric comparisons
-   Stability across time or validation slices
-   Data coverage drift

**Interpretation rule:** predictive importance describes how a model
uses information; it does not establish that a feature causes
viewership.

## SQL analytics

The project contains **25 SQL analysis modules**:

`quality` · `global_performance` · `country_performance` ·
`title_performance` · `lifecycle` · `retention` · `churn` · `momentum` ·
`breakouts` · `concentration` · `cohorts` · `market_intelligence` ·
`global_country_comparison` · `rank_analysis` · `views_analysis` ·
`hours_analysis` · `runtime_analysis` · `title_stability` ·
`market_breadth` · `content_mix` · `weekly_trends` · `entry_analysis` ·
`survival_analysis` · `forecast_features` · `model_performance_drift`.

**Reported audit result:** 25/25 SQL analyses passed.

## Dashboard

The Streamlit dashboard is organized into 13 analytical pages.

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
1.  Executive Overview
2.  Weekly Briefing
3.  Title Explorer
4.  Global & Cohorts
5.  Country Intelligence
6.  Entry / Retention / Churn
7.  Lifecycle & Concentration

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
8.  Breakouts & Momentum
9.  Forecasting & Model Stability
10. Statistical Evidence
11. Catalog & Metadata
12. Most Popular & H1 2026
13. Data Quality & Provenance

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
The dashboard source and query contracts were reported as validated in
the supplied audit. A live Streamlit HTTP smoke test was **not**
completed in that audit environment because Streamlit was unavailable
there.

## Data quality and provenance

Data validation is part of the analytical workflow, not an afterthought.

  Quality metric              Reported audit result
  ------------------------- -----------------------
  Source-grain integrity                       100%
  Global view coverage                       62.77%
  Global runtime coverage                    62.77%
  Global hours coverage                        100%
  TMDB entity coverage                       51.92%
  Metric validity                              100%
  Title completeness                           100%

The supplied validation summary reports:

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}37 /
37`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Tests
passed`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}25 / 25`</strong>`{=html}`<br>`{=html}`<sub>`{=html}SQL
analyses passed`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}64 /
64`</strong>`{=html}`<br>`{=html}`<sub>`{=html}Manifest hashes
matched`</sub>`{=html}
```{=html}
</td>
```
```{=html}
<td align="center" width="25%">
```
`<strong>`{=html}OK`</strong>`{=html}`<br>`{=html}`<sub>`{=html}SQLite
integrity`</sub>`{=html}
```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
Additional reported checks: Python compilation passed; no duplicate
global or country grain was detected; no negative metrics, hardcoded
local paths, stale v7 source references, TODO/FIXME markers, or cache
files were found in the audited final project.

A pipeline run generates `reports/pipeline_run_manifest.json`, recording
source, asset, and output information with SHA-256 hashes. Duplicate
aliases are checked so alternate references to the same official source
are not counted as unique facts.

> **Audit qualification:** these are results reported by the supplied
> project documentation, not freshly re-run as part of this README
> rewrite. Do not claim that `make verify` has just succeeded unless it
> has been run to completion in the target environment.

## Get started

### 1. Clone the repository

Replace the placeholders with the actual GitHub repository URL and
folder name.

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create and activate a virtual environment

**Linux / macOS**

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

``` powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

``` bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Download the official weekly datasets

``` bash
mkdir -p data/raw

curl -L \
  "https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
  -o data/raw/all-weeks-global.tsv

curl -L \
  "https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
  -o data/raw/all-weeks-countries.tsv
```

Inspect the files:

``` bash
ls -lh data/raw/
```

The supplied audit also used Most Popular source aliases and optional
legacy TMDB / H1 2026 reference assets. If the current pipeline requires
these inputs, obtain them from the sources and documentation referenced
by the repository before attempting a complete rebuild.

### 5. Run the pipeline and checks

``` bash
make build
make validate
make analysis
make test
make verify
```

The supplied Makefile description says `make verify` runs the pipeline
and then the automated test suite. Run it locally and inspect the exit
status before claiming fresh successful verification.

### 6. Launch the dashboard

``` bash
make dashboard
```

Equivalent command:

``` bash
python -m streamlit run dashboard/app.py
```

Open the local URL printed by Streamlit.

### Useful commands

  Command            Purpose
  ------------------ ----------------------------------------------------
  `make build`       Run the pipeline
  `make validate`    Run validation
  `make analysis`    Run analysis
  `make test`        Run automated tests
  `make dashboard`   Launch Streamlit
  `make verify`      Rebuild, then run tests
  `make clean`       Remove generated outputs according to the Makefile

## Repository structure

``` text
netflix_v8_1/
├── assets/                 # README figures and reference visuals
├── data/
│   ├── raw/                # Local source files; do not commit
│   └── processed/          # Locally generated data; do not commit
├── dashboard/
│   └── app.py
├── docs/
│   ├── methodology.md
│   ├── limitations.md
│   ├── data_dictionary.md
│   ├── data_model.md
│   ├── lineage.md
│   └── schema_contract.json
├── reports/                # Local generated outputs; do not commit
├── scripts/
│   └── run_pipeline.py
├── sql/                    # 25 SQL analysis modules
├── src/
│   ├── config.py
│   ├── validation.py
│   ├── pipeline.py
│   ├── analysis.py
│   └── advanced.py
├── tests/
│   └── test_project.py
├── Makefile
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

## GitHub data policy

Keep source data and generated analytical outputs out of version
control. Curated README images under `assets/` can remain in the
repository.

A suitable `.gitignore` should include:

``` gitignore
data/raw/*
data/processed/*
reports/*

*.csv
*.tsv
*.parquet
*.feather
*.db
*.sqlite
*.sqlite3

__pycache__/
*.py[cod]
.pytest_cache/
.venv/
.env
.DS_Store
```

Before pushing, inspect tracked files:

``` bash
git ls-files | grep -E '\.(csv|tsv|parquet|feather|db|sqlite|sqlite3)$'
```

This should return no tracked data/database files. If anything is
returned, review and remove those files from tracking before pushing.

## Business questions this project supports

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
**CONTENT & LIFECYCLE** - Which titles perform consistently rather than
relying on one peak? - Which titles show unusual acceleration? - How
long do titles remain observable in the Top 10? - Are lifecycle
estimates incomplete due to right-censoring?

**MARKETS & PORTFOLIO** - Which titles reach the most audience
markets? - Which markets show similar content patterns? - Is observed
engagement concentrated among a few titles? - Where does a title perform
strongly relative to its global results?

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
**FORECASTING & EVIDENCE** - Can recent behavior estimate next-week
views? - Does a model beat a naive baseline? - Are model errors stable
over time? - Are group differences statistically supported?

**TRUST & REPRODUCIBILITY** - Can data quality be checked before
analysis? - Are source aliases being double-counted? - Can results be
traced to input files? - Can the analysis be rebuilt without committing
source datasets?

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## Critical interpretation rules

1.  **Top 10 is not the full catalog.** A title absent from the dataset
    may still have viewers.
2.  **Audience market is not production country.** Country records
    describe the market represented by the measurement.
3.  **Missing is not zero.** Unavailable view metrics remain missing
    rather than being silently converted to zero.
4.  **TMDB is external metadata.** The reported entity match coverage is
    51.92%; this is not Netflix catalog coverage.
5.  **Prediction is not causation.** Forecasting and feature importance
    do not establish causal effects.
6.  **Observed lifecycle can be censored.** Titles still active at the
    end of the observation window may have longer real-world lifetimes.
7.  **Most Popular is a different measurement.** Its first-91-days
    ranking is not interchangeable with weekly Top 10 performance.
8.  **H1 2026 is a separate reference source.** It is not merged into
    weekly Top 10 fact tables.

## Limitations

This project does not claim to measure: - Total Netflix viewing across
the entire catalog - Viewing for titles that never enter the Top 10 -
The causes of a title's popularity - Production-country effects from
audience-market data - Complete real-world lifetimes for right-censored
titles - Complete Netflix catalog coverage from TMDB matching

The dataset begins in July 2021, and view/runtime availability is not
uniform across all records. Forecasting is limited to next-week views
for entities already observed in consecutive Top 10 weeks. Results are
observational and must be interpreted within these boundaries.

> **The central question:** What can we learn from Netflix's observed
> Top 10 measurements, and how reliably can those observations support
> analytical decisions?

## Skills demonstrated

```{=html}
<table>
```
```{=html}
<tr>
```
```{=html}
<td width="50%" valign="top">
```
**DATA ANALYTICS** - Exploratory analysis and KPI development - Trend
analysis, segmentation, and market intelligence - Lifecycle analysis and
business interpretation

**SQL** - Analytical queries and window functions - Cohort,
concentration, and survival analysis - Data-quality queries and model
diagnostics

**PYTHON** - Pandas, NumPy, and Scikit-learn - Statistical analysis -
Validation and pipeline development

```{=html}
</td>
```
```{=html}
<td width="50%" valign="top">
```
**MACHINE LEARNING** - Regression and forecasting - Random Forest and
HistGradientBoosting - Time-aware validation - Permutation importance
and SHAP - Forecast error and stability analysis

**DATA ENGINEERING** - Source contracts and normalization - Analytical
marts and SQLite - Provenance and SHA-256 hashes - Reproducible builds

**VISUALIZATION & ENGINEERING** - Streamlit, Matplotlib, and Plotly -
Pytest, Makefile workflows, Git, and documentation

```{=html}
</td>
```
```{=html}
</tr>
```
```{=html}
</table>
```
## Official references

-   [Netflix Top 10 portal](https://www.netflix.com/tudum/top10)
-   [Netflix Global Weekly Top 10
    data](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv)
-   [Netflix Country Weekly Top 10
    data](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv)
-   [Netflix Most
    Popular](https://www.netflix.com/tudum/top10/most-popular)
-   [Netflix: What We Watched --- First Half of
    2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026)

## Author

**Shubham Kumar Jha**\
Data Analytics · Business Analytics · Data Science · Scientific Data
Analysis

I build analytical projects that combine Python, SQL, statistics,
machine learning, visualization, and reproducible data workflows.

## Contribute

If this project is useful for learning, portfolio development, analytics
engineering, or content intelligence research:

-   Star the repository
-   Fork it and explore the methodology
-   Open an issue for bugs or improvements
-   Reproduce the analytical outputs and report discrepancies

## Disclaimer

This is an independent analytical project and is **not affiliated with,
sponsored by, or endorsed by Netflix**. Netflix and related trademarks
belong to their respective owners. The project uses publicly available
Netflix Top 10 data for analytical and educational purposes.

------------------------------------------------------------------------

::: {align="center"}
**Netflix Content Intelligence v8.1**

*Analyze · Validate · Explain · Forecast*

Python · SQL · Statistics · Machine Learning · Streamlit
:::
