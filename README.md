::: {align="center"}
# 🎬 Netflix Content Intelligence

### Source-Driven Netflix Top 10 Analytics • Global & Country Intelligence • Lifecycle • Forecasting • Machine Learning

```{=html}
<p align="center">
```
`<img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence" width="100%">`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
`<img src="https://img.shields.io/badge/Version-8.1-e50914?style=for-the-badge" alt="Version 8.1">`{=html}
`<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">`{=html}
`<img src="https://img.shields.io/badge/SQL-25%20Analyses-336791?style=for-the-badge" alt="SQL">`{=html}
`<img src="https://img.shields.io/badge/Tests-37%2F37%20Passing-2ea44f?style=for-the-badge" alt="Tests">`{=html}
`<img src="https://img.shields.io/badge/Markets-94-111827?style=for-the-badge" alt="Markets">`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
`<b>`{=html}An end-to-end analytics system built from Netflix's
published Top 10 data.`</b>`{=html}
```{=html}
</p>
```
```{=html}
<p>
```
Python • SQL • Pandas • Scikit-learn • Statistics • Forecasting • SQLite
• Streamlit
```{=html}
</p>
```
:::

------------------------------------------------------------------------

## 📌 What this project is

**Netflix Content Intelligence v8.1** is a source-driven analytics
project that rebuilds an analytical system from Netflix Top 10 data
rather than treating a static dataset as the final product.

The pipeline covers:

-   global weekly Top 10 performance
-   country-market intelligence
-   title/entity performance
-   entry, continuation, return and drop behavior
-   cohorts and lifecycle analysis
-   survival analysis with right-censoring
-   breakout and two-week momentum analysis
-   country similarity and concentration
-   statistical testing and Benjamini--Hochberg FDR
-   chronological next-week views forecasting
-   model stability, permutation importance and SHAP when available
-   SQL analytics
-   data-quality validation
-   provenance and reproducibility
-   an interactive Streamlit dashboard

### Core workflow

``` text
Official Netflix Sources
        ↓
Raw Ingestion
        ↓
Validation
        ↓
Normalization
        ↓
Analytical Marts + SQLite
        ↓
SQL + Statistics
        ↓
Lifecycle + Market Analytics
        ↓
Forecasting + ML
        ↓
Reports + Dashboard
```

------------------------------------------------------------------------

## 🚫 Data is intentionally NOT stored in this GitHub repository

This repository is designed to contain **code and documentation, not the
large datasets**.

Do not commit:

-   raw Netflix TSV/CSV files
-   processed CSV files
-   Parquet files
-   SQLite databases
-   generated analytical datasets

The data is downloaded from Netflix's official published sources and
generated locally.

> **Important:** the repository must be configured with a `.gitignore`
> that excludes `data/raw/`, `data/processed/`, `reports/`, `*.csv`,
> `*.tsv`, `*.parquet`, `*.db`, `*.sqlite`, and `*.sqlite3` before
> pushing to GitHub.

------------------------------------------------------------------------

# 📊 Project at a glance

```{=html}
<p align="center">
```
`<img src="assets/03_project_kpis.png" alt="Verified project KPIs" width="100%">`{=html}
```{=html}
</p>
```
  Metric                                              Verified scope
  ------------------------------ -----------------------------------
  Global weekly observations                              **10,960**
  Country weekly observations                            **510,340**
  Audience markets                                            **94**
  Weekly coverage                                      **274 weeks**
  Coverage period                        **2021-07-04 → 2026-09-27**
  Current Most Popular records                                **40**
  SQL analyses                                           **25 / 25**
  Automated tests                                        **37 / 37**
  Global source grain                               **40 rows/week**
  Country source grain             **10 rows/category/week/country**

------------------------------------------------------------------------

# 🧭 Contents

-   [What this project is](#-what-this-project-is)
-   [Data
    policy](#-data-is-intentionally-not-stored-in-this-github-repository)
-   [Project at a glance](#-project-at-a-glance)
-   [Official data sources](#-official-data-sources)
-   [Architecture](#-architecture)
-   [Analytical framework](#-analytical-framework)
-   [Global performance](#-global-performance)
-   [Country intelligence](#-country-intelligence)
-   [Lifecycle and survival](#-lifecycle-and-survival)
-   [Breakouts and momentum](#-breakouts-and-momentum)
-   [Statistical analysis](#-statistical-analysis)
-   [Forecasting and machine
    learning](#-forecasting-and-machine-learning)
-   [Dashboard](#-dashboard)
-   [SQL](#-sql-analytics)
-   [Data quality and provenance](#-data-quality-and-provenance)
-   [Installation](#-installation)
-   [Download the data](#-download-the-data)
-   [Run the pipeline](#-run-the-pipeline)
-   [Testing](#-testing)
-   [Repository structure](#-repository-structure)
-   [Interpretation rules](#-critical-interpretation-rules)
-   [Limitations](#-limitations)
-   [Skills demonstrated](#-skills-demonstrated)

------------------------------------------------------------------------

# 🗂️ Official data sources

## 1. Global weekly Top 10

Official Netflix source:

https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv

Download:

``` bash
mkdir -p data/raw

curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
-o data/raw/all-weeks-global.tsv
```

------------------------------------------------------------------------

## 2. Country weekly Top 10

Official Netflix source:

https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv

Download:

``` bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
-o data/raw/all-weeks-countries.tsv
```

------------------------------------------------------------------------

## 3. Netflix Most Popular

Official source:

https://www.netflix.com/tudum/top10/most-popular

The project treats the Most Popular ranking separately from weekly Top
10 performance.

The current all-time ranking is measured over the **first 91 days** of a
title's release window.

------------------------------------------------------------------------

## 4. Netflix Top 10 portal

Official source:

https://www.netflix.com/tudum/top10

Use this for the published Top 10 interface and methodology/context.

------------------------------------------------------------------------

## 5. What We Watched --- First Half of 2026

Official Netflix report:

https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026

The H1 2026 report is treated as a separate engagement reference and is
not silently merged into the weekly Top 10 fact tables.

------------------------------------------------------------------------

## Optional external metadata

The project can use the supplied legacy TMDB reference data for
enrichment.

It is explicitly classified as:

``` text
external_reference_not_catalog
```

It is **not** Netflix audience/performance data and is not treated as an
authoritative Netflix-wide catalog.

------------------------------------------------------------------------

# 🏗️ Architecture

```{=html}
<p align="center">
```
`<img src="assets/02_architecture.png" alt="Netflix Content Intelligence architecture" width="100%">`{=html}
```{=html}
</p>
```
``` text
┌─────────────────────────────────────────────┐
│            OFFICIAL NETFLIX DATA            │
│ Global • Countries • Most Popular           │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│                INGESTION                    │
│                  TSV / CSV                  │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│               VALIDATION                    │
│ Schema • Grain • Dates • Duplicates         │
│ Missingness • Metric validity               │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              NORMALIZATION                  │
│ Dates • Entity keys • Categories            │
│ Content type • Season / collection          │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│             ANALYTICAL LAYER                │
│        CSV marts + SQLite database          │
└──────────────┬─────────────────┬────────────┘
               │                 │
        ┌──────▼──────┐   ┌──────▼───────┐
        │     SQL     │   │  Statistics  │
        │ 25 analyses │   │ FDR / effect │
        └──────┬──────┘   └──────┬───────┘
               │                 │
               └────────┬────────┘
                        ▼
┌─────────────────────────────────────────────┐
│            ADVANCED ANALYTICS               │
│ Lifecycle • Survival • Concentration        │
│ Country Similarity • Breakouts              │
│ Forecasting • ML • Model Stability          │
└──────────────────────┬──────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────┐
│              OUTPUT LAYER                   │
│ Reports • Dashboard • CSV exports           │
└─────────────────────────────────────────────┘
```

------------------------------------------------------------------------

# 🔬 Analytical framework

## Performance

-   peak rank
-   average rank
-   peak views
-   peak hours
-   observed longevity
-   elapsed longevity
-   rank volatility
-   performance segmentation

## Lifecycle

-   new titles
-   continuing titles
-   returning titles
-   dropped titles
-   entry cohorts
-   weeks since entry
-   survival curves
-   right-censoring

## Market intelligence

-   country reach
-   title-market persistence
-   country similarity
-   Jaccard similarity
-   Top-1 / Top-3 / Top-10 concentration
-   HHI
-   country/title drilldowns

## Momentum

-   weekly movement
-   rank movement
-   exact two-week view acceleration
-   breakout detection

## Statistical evidence

-   association analysis
-   effect sizes
-   p-values
-   Benjamini--Hochberg FDR correction

## Predictive analytics

-   naive baseline
-   Ridge
-   Random Forest
-   HistGradientBoosting
-   permutation importance
-   SHAP when available
-   forecast error analysis
-   chronological model stability

------------------------------------------------------------------------

# 🌍 Global performance

```{=html}
<p align="center">
```
`<img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="92%">`{=html}
```{=html}
</p>
```
The global weekly fact contains **10,960 observations covering 274
weeks**.

The analytical layer examines:

-   weekly performance
-   rank trajectories
-   peak performance
-   title longevity
-   movement between weeks
-   title-level performance segments

The project does not interpret absence from Top 10 as zero Netflix
viewing.

------------------------------------------------------------------------

# 🗺️ Country intelligence

```{=html}
<p align="center">
```
`<img src="assets/05_country_coverage.png" alt="Country coverage" width="92%">`{=html}
```{=html}
</p>
```
The country fact contains **510,340 observations across 94 audience
markets**.

The analysis includes:

-   market reach
-   market persistence
-   title-market relationships
-   country similarity
-   concentration
-   country drilldowns
-   title drilldowns by market

### Important

`country_name` / country identifiers represent the **audience market
represented by the ranking**.

They are not production-country fields.

------------------------------------------------------------------------

# ⏳ Lifecycle and survival

The project tracks title/entity movement through the Top 10:

``` text
NEW
 │
 ├──► CONTINUING
 │
 ├──► DROPPED
 │
 └──► RETURNING
```

Lifecycle analysis uses:

-   first observed week
-   last observed week
-   observed weeks
-   elapsed calendar weeks
-   entry cohort
-   weeks since entry
-   return behavior

### Survival

Survival analysis uses elapsed calendar weeks and explicit
right-censoring.

A title still observed at the dataset boundary is not assigned an
artificial ending.

------------------------------------------------------------------------

# ⚡ Breakouts and momentum

Breakout detection uses **exact two-week intervals**.

This prevents the analysis from treating observations separated by
unknown gaps as consecutive.

The resulting analysis identifies:

-   two-week acceleration
-   large weekly movements
-   breakout candidates
-   momentum patterns

------------------------------------------------------------------------

# 📐 Statistical analysis

The statistical layer is designed to add evidence to descriptive
findings.

It includes:

``` text
Descriptive comparison
        ↓
Statistical test
        ↓
Effect size
        ↓
Benjamini–Hochberg FDR
        ↓
Interpretation
```

The output contains:

-   analysis name
-   statistical test
-   p-value
-   effect size
-   sample size
-   BH-adjusted q-value
-   FDR significance flag

Statistical significance is not treated as proof of causality.

------------------------------------------------------------------------

# 🤖 Forecasting and machine learning

## Target

The forecasting task is:

> **Next-week views for entities with consecutive Top 10 observations.**

This is a conditional forecasting problem.

It is **not** a model for predicting whether an arbitrary Netflix
catalog title will enter the Top 10.

------------------------------------------------------------------------

## Models

The benchmark includes:

-   Naive baseline
-   Ridge Regression
-   Random Forest
-   HistGradientBoosting

------------------------------------------------------------------------

## Validation

The audited model uses:

``` text
Chronological 80/20 holdout
Cutoff week: 2026-01-25
Training rows: 1,690
Test rows: 394
```

No random temporal shuffling is used.

------------------------------------------------------------------------

## Verified benchmark

The current project output reports:

  ------------------------------------------------------------------------------------------------------
  Model                                   MAE               RMSE           R²        sMAPE           MAE
                                                                                             improvement
                                                                                                vs naive
  -------------------------- ---------------- ------------------ ------------ ------------ -------------
  Naive                          4,818,781.73       7,693,942.50      -5.0073       0.7051          0.0%

  Ridge                          1,306,746.39       2,481,223.14       0.3752       0.3047        72.88%

  Random Forest                    772,008.52       1,811,793.36       0.6669       0.2018        83.98%

  **HistGradientBoosting**     **752,565.16**   **1,748,406.59**   **0.6898**   **0.1974**    **84.38%**
  ------------------------------------------------------------------------------------------------------

**Best non-naive model in this audited run: HistGradientBoosting.**

```{=html}
<p align="center">
```
`<img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="92%">`{=html}
```{=html}
</p>
```
These are out-of-sample predictive results for the defined conditional
forecasting task. They should not be interpreted causally.

------------------------------------------------------------------------

# 🧠 Model interpretability

The project includes:

-   permutation importance
-   forecast error analysis
-   model stability across chronological cutoffs
-   SHAP when available

Interpretation rule:

``` text
Predictive importance
        ≠
Causal effect
```

------------------------------------------------------------------------

# 🖥️ Streamlit dashboard

Run:

``` bash
make dashboard
```

The current dashboard contains these analysis pages:

1.  **Executive Overview**
2.  **Weekly Briefing**
3.  **Title Explorer**
4.  **Global & Cohorts**
5.  **Country Intelligence**
6.  **Entry / Retention / Churn**
7.  **Lifecycle & Concentration**
8.  **Breakouts & Momentum**
9.  **Forecasting & Model Stability**
10. **Statistical Evidence**
11. **Catalog & Metadata**
12. **Most Popular & H1 2026**
13. **Data Quality & Provenance**

The dashboard also provides downloadable analytical CSV views where
implemented.

------------------------------------------------------------------------

# 🧮 SQL analytics

The repository contains **25 SQL analysis files**.

They cover:

-   data quality
-   title performance
-   weekly movement
-   lifecycle
-   cohorts
-   concentration
-   country intelligence
-   country similarity
-   title-market relationships
-   survival
-   breakouts
-   release-age analysis
-   statistical outputs
-   forecasting
-   forecast errors
-   model diagnostics
-   model stability
-   data drift
-   model-performance drift
-   provenance

The project records SQL execution results in:

``` text
reports/sql_execution_report.json
```

The audited output reports:

``` text
25 SQL files
25 passed
```

------------------------------------------------------------------------

# 🛡️ Data quality and provenance

```{=html}
<p align="center">
```
`<img src="assets/07_data_quality.png" alt="Data quality scorecard" width="92%">`{=html}
```{=html}
</p>
```
The current data-quality scorecard contains these verified metrics:

  Metric                           Score
  ------------------------- ------------
  Source grain integrity        **100%**
  Global view coverage        **62.77%**
  Global runtime coverage     **62.77%**
  Global hours coverage         **100%**
  TMDB entity coverage        **51.92%**
  Metric validity               **100%**
  Title completeness            **100%**

### What these numbers mean

**Global view coverage is 62.77%** because Netflix's published weekly
views are not available for every historical observation.

Those unavailable values are kept missing.

They are **not converted to zero**.

**TMDB entity coverage is 51.92%** and is explicitly an external
metadata match rate. It is **not Netflix catalog coverage**.

------------------------------------------------------------------------

# 🔐 Provenance

Each build generates:

``` text
reports/pipeline_run_manifest.json
```

The manifest records source, asset and output information with SHA-256
hashes.

The pipeline also validates duplicate aliases.

For the audited source set:

``` text
Global weekly aliases:
NOT counted as unique facts

Most Popular aliases:
NOT counted as unique facts
```

------------------------------------------------------------------------

# 🧪 Testing

Run:

``` bash
make test
```

The project test suite contains **37 tests**.

The audited result is:

``` text
37 / 37 passing
```

Tests cover:

-   source file contracts
-   global row counts
-   country row counts
-   date ranges
-   weekly grain
-   duplicate source aliases
-   missing-view semantics
-   negative metric checks
-   processed output contracts
-   title mart contracts
-   country similarity bounds
-   survival bounds
-   forecast model presence
-   chronological validation
-   breakout contracts
-   statistical output contracts
-   H1 2026 reference table
-   SQL execution
-   SQLite table contracts
-   provenance manifest
-   data-quality zero-error checks
-   schema contracts
-   Python compilation
-   v8 advanced outputs
-   FDR columns
-   catalog-source classification
-   dashboard contracts
-   stale-v7-path checks

------------------------------------------------------------------------

# ⚙️ Installation

## Clone

``` bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git

cd YOUR_REPOSITORY
```

## Create a virtual environment

### Linux / macOS

``` bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

``` powershell
python -m venv .venv
.venv\Scripts\activate
```

## Install dependencies

``` bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

------------------------------------------------------------------------

# 📥 Download the data

Create the local raw-data directory:

``` bash
mkdir -p data/raw
```

Download the official global dataset:

``` bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
-o data/raw/all-weeks-global.tsv
```

Download the official country dataset:

``` bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
-o data/raw/all-weeks-countries.tsv
```

Then inspect:

``` bash
ls -lh data/raw/
```

### Expected core files

``` text
data/raw/
├── all-weeks-global.tsv
└── all-weeks-countries.tsv
```

The current audited build also used the current Most Popular aliases and
optional legacy TMDB/H1 2026 reference assets.

If those optional/source-specific files are required by the current
pipeline version, obtain them from the source package or official source
referenced by the project documentation before running a full rebuild.

------------------------------------------------------------------------

# 🔄 Run the pipeline

The Makefile provides:

``` bash
make build
```

which runs:

``` bash
python3 scripts/run_pipeline.py
```

Other commands:

``` bash
make validate
make analysis
make test
make dashboard
make verify
make clean
```

### Full verification

``` bash
make verify
```

The current Makefile implementation runs:

``` text
python scripts/run_pipeline.py
        ↓
python -m pytest
```

So `make verify` is a rebuild followed by the automated test suite.

------------------------------------------------------------------------

# 🖥️ Run the dashboard

``` bash
make dashboard
```

Equivalent command:

``` bash
python -m streamlit run dashboard/app.py
```

------------------------------------------------------------------------

# 📁 Repository structure

``` text
netflix_v8_1/
│
├── assets/
│   ├── 01_hero_banner.png
│   ├── 02_architecture.png
│   ├── 03_project_kpis.png
│   ├── 04_global_weekly_views.png
│   ├── 05_country_coverage.png
│   ├── 06_forecast_benchmark.png
│   └── 07_data_quality.png
│
├── data/
│   ├── raw/                    # local source data; do not commit
│   └── processed/              # generated locally; do not commit
│
├── dashboard/
│   └── app.py
│
├── docs/
│   ├── methodology.md
│   ├── limitations.md
│   ├── data_dictionary.md
│   ├── data_model.md
│   ├── lineage.md
│   └── schema_contract.json
│
├── reports/                    # generated locally; do not commit
│
├── scripts/
│   └── run_pipeline.py
│
├── sql/                        # 25 executable SQL analyses
│
├── src/
│   ├── config.py
│   ├── validation.py
│   ├── pipeline.py
│   └── analysis.py
│
├── tests/
│   └── test_project.py
│
├── Makefile
├── pyproject.toml
├── requirements.txt
├── .gitignore
└── README.md
```

------------------------------------------------------------------------

# 🚫 GitHub data policy

Before pushing this repository, make sure the GitHub repository does not
contain:

``` text
data/raw/*.tsv
data/raw/*.csv
data/processed/*.csv
data/processed/*.db
data/processed/*.sqlite
reports/*.csv
reports/*.json
```

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

The README visuals under `assets/` are intentionally small, curated
presentation assets and are safe to keep with the repository.

------------------------------------------------------------------------

# ⚠️ Critical interpretation rules

## 1. Top 10 is not the complete Netflix catalog

A title absent from the Top 10 dataset is not equivalent to zero
viewing.

------------------------------------------------------------------------

## 2. Country is an audience market

Country observations represent the market in which the ranking was
observed.

They are not production-country measurements.

------------------------------------------------------------------------

## 3. Missing views are not zero

Historical Netflix Top 10 records can have unavailable view metrics.

The pipeline preserves those values as missing.

------------------------------------------------------------------------

## 4. TMDB is external metadata

TMDB enrichment is not Netflix audience data.

The current external metadata match rate is **51.92% at the entity
level** in the audited build.

------------------------------------------------------------------------

## 5. Prediction is not causation

Forecasting and feature importance identify predictive relationships.

They do not establish causal effects.

------------------------------------------------------------------------

## 6. Survival observations are censored

Titles still observed at the end of the available time window are
right-censored.

------------------------------------------------------------------------

## 7. Most Popular is a separate measurement

The Most Popular all-time ranking is measured over the first 91 days and
should not be interpreted as the same metric as weekly Top 10
performance.

------------------------------------------------------------------------

# ⚠️ Limitations

This project does not claim to measure:

-   the complete Netflix catalog
-   total Netflix viewing across all Netflix titles
-   performance of titles that never appear in the Top 10
-   causal drivers of popularity
-   production-country effects from audience-market data
-   missing views as zero
-   TMDB popularity as Netflix popularity

The detailed methodology and limitations are documented in:

``` text
docs/methodology.md
docs/limitations.md
```

------------------------------------------------------------------------

# 💼 Skills demonstrated

### Data Analytics

-   Exploratory Data Analysis
-   KPI development
-   Trend analysis
-   Segmentation
-   Market intelligence
-   Lifecycle analysis
-   Business-oriented interpretation

### SQL

-   Analytical SQL
-   Window functions
-   Cohort analysis
-   Concentration metrics
-   HHI
-   Data-quality queries
-   Model diagnostics
-   Drift analysis

### Python

-   Pandas
-   NumPy
-   Scikit-learn
-   Data validation
-   Statistical analysis
-   ETL/pipeline development

### Machine Learning

-   Regression
-   Forecasting
-   Random Forest
-   HistGradientBoosting
-   Time-aware validation
-   Permutation importance
-   SHAP
-   Forecast error analysis
-   Model stability

### Data Engineering

-   Source contracts
-   Data normalization
-   Analytical marts
-   SQLite
-   Provenance
-   SHA-256 hashing
-   Reproducible builds

### Visualization / BI

-   Streamlit
-   Matplotlib
-   Plotly
-   Executive KPI design
-   Interactive drilldowns
-   Analytical exports

### Engineering

-   Pytest
-   Automated validation
-   Configuration
-   Makefile workflows
-   Git/GitHub
-   Documentation
-   Reproducibility

------------------------------------------------------------------------

# 🎯 Business questions this project supports

### Content

> Which titles perform consistently instead of relying on a single peak?

### Lifecycle

> How long do titles remain observable in the Top 10?

### Markets

> Which titles achieve broad market reach?

### Concentration

> Is a title's observed performance concentrated in a small number of
> markets?

### Momentum

> Which titles show unusual two-week acceleration?

### Forecasting

> Can recent Top 10 behavior help estimate next-week views?

### Data quality

> Can analytical results be traced back to validated source data?

------------------------------------------------------------------------

# 🖼️ Project visuals

## Architecture

```{=html}
<p align="center">
```
`<img src="assets/02_architecture.png" alt="Netflix analytics architecture" width="100%">`{=html}
```{=html}
</p>
```
## Project scale

```{=html}
<p align="center">
```
`<img src="assets/03_project_kpis.png" alt="Netflix project scale" width="100%">`{=html}
```{=html}
</p>
```
## Global activity

```{=html}
<p align="center">
```
`<img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="92%">`{=html}
```{=html}
</p>
```
## Country coverage

```{=html}
<p align="center">
```
`<img src="assets/05_country_coverage.png" alt="Country coverage" width="92%">`{=html}
```{=html}
</p>
```
## Forecast benchmark

```{=html}
<p align="center">
```
`<img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="92%">`{=html}
```{=html}
</p>
```
## Data quality

```{=html}
<p align="center">
```
`<img src="assets/07_data_quality.png" alt="Data quality scorecard" width="92%">`{=html}
```{=html}
</p>
```

------------------------------------------------------------------------

# 🏁 Final takeaway

**Netflix Content Intelligence v8.1 is an end-to-end analytics system,
not just a visualization project.**

It combines:

``` text
Official source data
       +
Validation
       +
Normalization
       +
Analytical modeling
       +
SQL
       +
Statistics
       +
Lifecycle analysis
       +
Market intelligence
       +
Forecasting
       +
Machine Learning
       +
Interpretability
       +
Dashboarding
       +
Testing
       +
Provenance
```

The project is deliberately conservative about what the data can prove:

``` text
Observed Top 10 performance
          ≠
Complete Netflix viewing
          ≠
Prediction
          ≠
Causation
```

That distinction is central to the design of the project.

------------------------------------------------------------------------

::: {align="center"}
# 🎬 Netflix Content Intelligence v8.1

### Analyze • Validate • Explain • Forecast

**Python · SQL · Statistics · Machine Learning · Streamlit**
:::
