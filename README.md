<div align="center">

# 🎬 Netflix Content Intelligence

### Source-Driven Netflix Top 10 Analytics • Global & Country Intelligence • Lifecycle • Forecasting • Machine Learning

<p align="center">
<img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence" width="100%">
</p>

<p>
<img src="https://img.shields.io/badge/Version-8.1-e50914?style=for-the-badge" alt="Version 8.1">
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
<img src="https://img.shields.io/badge/SQL-25%20Analyses-336791?style=for-the-badge" alt="SQL">
<img src="https://img.shields.io/badge/Tests-37%2F37%20Passing-2ea44f?style=for-the-badge" alt="Tests">
<img src="https://img.shields.io/badge/Markets-94-111827?style=for-the-badge" alt="Markets">
</p>

<p><b>An end-to-end analytics system built from Netflix's published Top 10 data.</b></p>

<p>Python • SQL • Pandas • Scikit-learn • Statistics • Forecasting • SQLite • Streamlit</p>

</div>

---

## 📌 What This Project Is

**Netflix Content Intelligence v8.1** is a source-driven analytics project that rebuilds an analytical system from Netflix Top 10 data rather than treating a static dataset as the final product.

The pipeline covers:

- Global weekly Top 10 performance
- Country-market intelligence
- Title/entity performance
- Entry, continuation, return and drop behavior
- Cohorts and lifecycle analysis
- Survival analysis with right-censoring
- Breakout and two-week momentum analysis
- Country similarity and concentration
- Statistical testing and Benjamini-Hochberg FDR
- Chronological next-week views forecasting
- Model stability, permutation importance and SHAP when available
- SQL analytics
- Data-quality validation
- Provenance and reproducibility
- Interactive Streamlit dashboard

### Core Workflow

```text
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

---

# 🚫 Data Is Intentionally NOT Stored in This GitHub Repository

> **Repository requirement:** keep the `assets/` folder in the repository because the README references the seven project visuals below. The large datasets and generated analytical outputs should remain local and ignored by Git.

This repository is designed to contain **code and documentation, not the large datasets**.

Do not commit:

- Raw Netflix TSV/CSV files
- Processed CSV files
- Parquet files
- SQLite databases
- Generated analytical datasets

The data is downloaded from Netflix's official published sources and generated locally.

> **Important:** the repository must be configured with a `.gitignore` that excludes `data/raw/`, `data/processed/`, `reports/`, `*.csv`, `*.tsv`, `*.parquet`, `*.db`, `*.sqlite`, and `*.sqlite3` before pushing to GitHub.

---

# 📊 Project at a Glance

<p align="center">
  <img src="assets/03_project_kpis.png" alt="Verified project KPIs" width="100%">
</p>

| Metric | Verified Scope |
|---|---:|
| Global weekly observations | **10,960** |
| Country weekly observations | **510,340** |
| Audience markets | **94** |
| Weekly coverage | **274 weeks** |
| Coverage period | **2021-07-04 → 2026-09-27** |
| Current Most Popular records | **40** |
| SQL analyses | **25 / 25** |
| Automated tests | **37 / 37** |
| Global source grain | **40 rows/week** |
| Country source grain | **10 rows/category/week/country** |

---

# 🧭 Contents

- [What This Project Is](#-what-this-project-is)
- [Data Policy](#-data-is-intentionally-not-stored-in-this-github-repository)
- [Project at a Glance](#-project-at-a-glance)
- [Official Data Sources](#-official-data-sources)
- [Architecture](#-architecture)
- [Analytical Framework](#-analytical-framework)
- [Global Performance](#-global-performance)
- [Country Intelligence](#-country-intelligence)
- [Lifecycle and Survival](#-lifecycle-and-survival)
- [Breakouts and Momentum](#-breakouts-and-momentum)
- [Statistical Analysis](#-statistical-analysis)
- [Forecasting and Machine Learning](#-forecasting-and-machine-learning)
- [Dashboard](#-dashboard)
- [SQL Analytics](#-sql-analytics)
- [Data Quality and Provenance](#-data-quality-and-provenance)
- [Installation](#-installation)
- [Download the Data](#-download-the-data)
- [Run the Pipeline](#-run-the-pipeline)
- [Testing](#-testing)
- [Repository Structure](#-repository-structure)
- [Interpretation Rules](#-critical-interpretation-rules)
- [Limitations](#-limitations)
- [Skills Demonstrated](#-skills-demonstrated)

---

# 🗂️ Official Data Sources

## 1. Global Weekly Top 10

Official Netflix source:

https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv

Download:

```bash
mkdir -p data/raw

curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
-o data/raw/all-weeks-global.tsv
```

---

## 2. Country Weekly Top 10

Official Netflix source:

https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv

Download:

```bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
-o data/raw/all-weeks-countries.tsv
```

---

## 3. Netflix Most Popular

Official source:

https://www.netflix.com/tudum/top10/most-popular

The project treats the Most Popular ranking separately from weekly Top 10 performance.

The current all-time ranking is measured over the **first 91 days** of a title's release window.

---

## 4. Netflix Top 10 Portal

Official source:

https://www.netflix.com/tudum/top10

Use this for the published Top 10 interface and methodology/context.

---

## 5. What We Watched — First Half of 2026

Official Netflix report:

https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026

The H1 2026 report is treated as a separate engagement reference and is not silently merged into the weekly Top 10 fact tables.

---

## Optional External Metadata

The project can use the supplied legacy TMDB reference data for enrichment.

It is explicitly classified as:

```text
external_reference_not_catalog
```

It is **not** Netflix audience/performance data and is not treated as an authoritative Netflix-wide catalog.

---

# 🏗️ Architecture

<p align="center">
<img src="assets/02_architecture.png" alt="Netflix Content Intelligence architecture" width="100%">
</p>

```text
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

---

# 🔬 Analytical Framework

## Performance

- Peak rank
- Average rank
- Peak views
- Peak hours
- Observed longevity
- Elapsed longevity
- Rank volatility
- Performance segmentation

## Lifecycle

- New titles
- Continuing titles
- Returning titles
- Dropped titles
- Entry cohorts
- Weeks since entry
- Survival curves
- Right-censoring

## Market Intelligence

- Country reach
- Title-market persistence
- Country similarity
- Jaccard similarity
- Top-1 / Top-3 / Top-10 concentration
- HHI
- Country/title drilldowns

## Momentum

- Weekly movement
- Rank movement
- Exact two-week view acceleration
- Breakout detection

## Statistical Evidence

- Association analysis
- Effect sizes
- P-values
- Benjamini-Hochberg FDR correction

## Predictive Analytics

- Naive baseline
- Ridge
- Random Forest
- HistGradientBoosting
- Permutation importance
- SHAP when available
- Forecast error analysis
- Chronological model stability

---

# 🌍 Global Performance

<p align="center">
<img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="92%">
</p>

The global weekly fact contains **10,960 observations covering 274 weeks**.

The analytical layer examines:

- Weekly performance
- Rank trajectories
- Peak performance
- Title longevity
- Movement between weeks
- Title-level performance segments

The project does not interpret absence from Top 10 as zero Netflix viewing.

---

# 🗺️ Country Intelligence

<p align="center">
<img src="assets/05_country_coverage.png" alt="Country coverage" width="92%">
</p>

The country-level fact contains:

- **510,340 observations**
- **94 audience markets**
- **274 weeks**

The country layer supports analysis of:

- Market-specific performance
- Geographic reach
- Title-market persistence
- Cross-market breakouts
- Market concentration
- Country similarity
- International content distribution

### Country Grain

The audited source grain is:

```text
10 rows / category / week / country
```

The country dimension represents the **audience market represented by Netflix's dataset**.

It should not automatically be interpreted as:

```text
Country of production
```

or:

```text
Country of origin
```

---

# 🔄 Lifecycle and Survival

The project treats title lifecycle as a sequence of weekly observations.

### Entry

The first observed appearance of a title/entity in the relevant Top 10 dataset.

### Continuation

A title that remains observable in consecutive weeks.

### Return

A title that reappears after an observed gap.

### Drop

A title that is no longer observed after its active run.

### Retention

The number of observed weeks a title remains active.

### Survival

The probability of remaining observable through successive periods.

---

## Right-Censoring

Lifecycle analysis is subject to **right-censoring** at the end of the observation period.

A title still active in the final available week has not necessarily completed its actual lifecycle.

Therefore:

```text
Observed survival
        ≠
Complete real-world lifetime
```

This distinction is explicitly preserved in the analysis.

---

# 🚀 Breakouts and Momentum

The project identifies titles showing meaningful short-term movement.

Examples include:

- Rank acceleration
- View acceleration
- Strong week-over-week growth
- Two-week momentum
- New entries
- Cross-market expansion
- Sustained performance

The objective is not simply to identify the largest titles.

The objective is to identify:

> **titles whose trajectory is changing.**

---

# 🧪 Statistical Analysis

The project goes beyond descriptive charts by applying statistical analysis to selected analytical questions.

Methods include:

- Distribution analysis
- Group comparison
- Association analysis
- Effect-size analysis
- Hypothesis testing
- Multiple-testing correction
- Benjamini-Hochberg false discovery rate control

Where applicable, the analysis reports:

- Sample size
- Test statistic
- P-value
- Adjusted P-value
- Effect size
- Practical interpretation

Statistical significance is not treated as equivalent to business importance.

---

# 🎯 Forecasting and Machine Learning

The forecasting task is intentionally constrained.

The project predicts:

> **Next-week views for entities with consecutive Top 10 observations.**

It does **not** attempt to predict whether an arbitrary title will enter the Top 10.

This distinction is important because the available data directly supports a next-week continuation forecasting task more cleanly than a complete future-entry prediction task.

---

## Chronological Validation

The final benchmark uses an **80/20 chronological holdout**.

```text
Historical observations
───────────────────────────────────────────────→ Time

          TRAIN                     TEST
           80%                       20%
────────────────────────────┬──────────────────
                            │
                      2026-01-25
                         cutoff
```

### Audited Split

| Metric | Value |
|---|---:|
| Cutoff week | **2026-01-25** |
| Training rows | **1,690** |
| Test rows | **394** |
| Validation strategy | **Chronological 80/20** |

Randomly mixing future observations into training would create temporal leakage, so the final holdout preserves time ordering.

---

# 🏆 Forecast Benchmark

<p align="center">
<img src="assets/06_forecast_benchmark.png" alt="Forecast model benchmark" width="92%">
</p>

| Model | MAE | RMSE | R² | sMAPE | Improvement |
|---|---:|---:|---:|---:|---:|
| Naive | 4,818,781.73 | 7,693,942.50 | -5.0073 | 0.7051 | 0% |
| Ridge | 1,306,746.39 | 2,481,223.14 | 0.3752 | 0.3047 | 72.88% |
| Random Forest | 772,008.52 | 1,811,793.36 | 0.6669 | 0.2018 | 83.98% |
| **HistGradientBoosting** | **752,565.16** | **1,748,406.59** | **0.6898** | **0.1974** | **84.38%** |

### Best Non-Naive Model

**HistGradientBoosting**

Audited performance:

- MAE: **752,565.16**
- RMSE: **1,748,406.59**
- R²: **0.6898**
- sMAPE: **0.1974**
- Improvement over naive: **84.38%**

These results describe predictive performance on the defined holdout task.

They should not be interpreted as causal evidence.

---

# 🔎 Model Interpretation

The project supports model diagnostics including:

- Feature importance
- Permutation importance
- SHAP when available
- Error distributions
- Stability analysis
- Drift analysis
- Model comparison

### Important interpretation rule

Predictive importance does not establish causality.

For example:

```text
Feature is predictive
        ≠
Feature causes views
```

The model is used for prediction and analytical understanding, not causal inference.

---

# 🖥️ Dashboard

The Streamlit dashboard contains **13 analytical pages**.

## 1. Executive Overview

High-level KPIs and overall performance.

## 2. Weekly Briefing

Weekly movement and notable changes.

## 3. Title Explorer

Detailed title/entity exploration.

## 4. Global & Cohorts

Global performance and cohort comparisons.

## 5. Country Intelligence

Market-specific performance and geographic analysis.

## 6. Entry / Retention / Churn

Lifecycle and persistence analysis.

## 7. Lifecycle & Concentration

Survival, concentration and content dependency.

## 8. Breakouts & Momentum

Emerging titles and performance acceleration.

## 9. Forecasting & Model Stability

Forecast predictions, benchmarks and diagnostics.

## 10. Statistical Evidence

Statistical tests and supporting evidence.

## 11. Catalog & Metadata

Metadata enrichment and catalog analysis.

## 12. Most Popular & H1 2026

Most Popular analysis and H1 2026 reporting.

## 13. Data Quality & Provenance

Data-quality checks, source lineage and provenance.

---

# 🗃️ SQL Analytics

The project contains **25 SQL analytical modules**.

```text
01_quality.sql
02_global_performance.sql
03_country_performance.sql
04_title_performance.sql
05_lifecycle.sql
06_retention.sql
07_churn.sql
08_momentum.sql
09_breakouts.sql
10_concentration.sql
11_cohorts.sql
12_market_intelligence.sql
13_global_country_comparison.sql
14_rank_analysis.sql
15_views_analysis.sql
16_hours_analysis.sql
17_runtime_analysis.sql
18_title_stability.sql
19_market_breadth.sql
20_content_mix.sql
21_weekly_trends.sql
22_entry_analysis.sql
23_survival_analysis.sql
24_forecast_features.sql
25_model_performance_drift.sql
```

The audited result is:

```text
25 / 25 SQL analyses passed
```

The SQL layer covers:

- Data quality
- Global performance
- Country performance
- Title performance
- Lifecycle
- Retention
- Churn
- Momentum
- Breakouts
- Concentration
- Cohorts
- Market intelligence
- Ranking
- Views
- Hours
- Runtime
- Stability
- Market breadth
- Content mix
- Weekly trends
- Entry
- Survival
- Forecast features
- Model performance
- Model drift

---

# 📊 Data Quality and Provenance

<p align="center">
<img src="assets/07_data_quality.png" alt="Data quality scorecard" width="92%">
</p>

Data quality is treated as a first-class part of the system.

## Audited Quality Metrics

| Quality Metric | Result |
|---|---:|
| Source grain integrity | **100%** |
| Global view coverage | **62.77%** |
| Global runtime coverage | **62.77%** |
| Global hours coverage | **100%** |
| TMDB entity coverage | **51.92%** |
| Metric validity | **100%** |
| Title completeness | **100%** |

---

# 🧪 Validation Results

The current audited build reports:

```text
37 / 37 automated tests passed
25 / 25 SQL analyses passed
64 / 64 manifest hashes matched
SQLite integrity: OK
Python compilation: PASSED
Global duplicate grain: NONE
Country duplicate grain: NONE
Negative metrics: NONE
Hardcoded local paths: NONE
Stale v7 source references: NONE
TODO/FIXME in source: NONE
Cache files in final project: NONE
```

---

# 🔐 Provenance

Each build generates:

```text
reports/pipeline_run_manifest.json
```

The manifest records source, asset and output information with SHA-256 hashes.

The pipeline also validates duplicate aliases.

For the audited source set:

```text
Global weekly aliases:
NOT counted as unique facts

Most Popular aliases:
NOT counted as unique facts
```

This prevents duplicate official-source aliases from being incorrectly double-counted.

---

# 📦 Current Audited Data Scope

The latest audited build contains:

```text
Global weekly observations     10,960
Country weekly observations   510,340
Audience markets                   94
Weeks                              274
Date range               2021-07-04 → 2026-09-27
Most Popular records               40
SQL analyses                       25
Automated tests                    37
```

### Global Source Grain

```text
40 rows / week
```

### Country Source Grain

```text
10 rows / category / week / country
```

These grain rules are explicitly validated.

---

# ⚙️ Installation

## Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

## Create a Virtual Environment

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
```

## Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

---

# 📥 Download the Data

Create the local raw-data directory:

```bash
mkdir -p data/raw
```

Download the official global dataset:

```bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
-o data/raw/all-weeks-global.tsv
```

Download the official country dataset:

```bash
curl -L \
"https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
-o data/raw/all-weeks-countries.tsv
```

Inspect the files:

```bash
ls -lh data/raw/
```

### Expected Core Files

```text
data/raw/
├── all-weeks-global.tsv
└── all-weeks-countries.tsv
```

The current audited build also used the current Most Popular aliases and optional legacy TMDB/H1 2026 reference assets.

If those optional/source-specific files are required by the current pipeline version, obtain them from the source package or official source referenced by the project documentation before running a full rebuild.

---

# 🔄 Run the Pipeline

The Makefile provides:

```bash
make build
```

which runs:

```bash
python3 scripts/run_pipeline.py
```

Other commands:

```bash
make validate
make analysis
make test
make dashboard
make verify
make clean
```

### Full Verification

```bash
make verify
```

The Makefile implementation runs:

```text
python scripts/run_pipeline.py
        ↓
python -m pytest
```

So `make verify` performs a rebuild followed by the automated test suite.

> **Audit note:** the latest independent validation confirmed the underlying tests, SQL analyses, manifest hashes, SQLite integrity and compilation separately. A full `make verify` completion should not be claimed unless it has been freshly executed to completion in the current environment.

---

# 🖥️ Run the Dashboard

```bash
make dashboard
```

Equivalent command:

```bash
python -m streamlit run dashboard/app.py
```

Then open the local Streamlit URL shown by the command.

> The dashboard source and underlying database/query contracts were validated. A live Streamlit HTTP smoke test was not completed in the execution environment used for the latest audit because Streamlit was unavailable there.

---

# 🧪 Testing

Run:

```bash
make test
```

Or:

```bash
pytest -q
```

The project test suite contains **37 tests**.

Audited result:

```text
37 / 37 passing
```

Tests cover:

- Source file contracts
- Global row counts
- Country row counts
- Date ranges
- Weekly grain
- Duplicate source aliases
- Missing-view semantics
- Negative metric checks
- Processed output contracts
- Title mart contracts
- Country similarity bounds
- Survival bounds
- Forecast model presence
- Chronological validation
- Breakout contracts
- Statistical output contracts
- H1 2026 reference table
- SQL execution
- SQLite table contracts
- Provenance manifest
- Data-quality zero-error checks
- Schema contracts
- Python compilation
- Advanced analytical outputs
- FDR columns
- Catalog-source classification
- Dashboard contracts
- Stale-v7-path checks

---

# 📁 Repository Structure

```text
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
│   ├── __init__.py
│   ├── config.py
│   ├── validation.py
│   ├── pipeline.py
│   ├── analysis.py
│   └── advanced.py
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

---

# 🚫 GitHub Data Policy

Before pushing this repository, make sure the GitHub repository does not contain:

```text
data/raw/*.tsv
data/raw/*.csv
data/processed/*.csv
data/processed/*.db
data/processed/*.sqlite
reports/*.csv
reports/*.json
```

A suitable `.gitignore` should include:

```gitignore
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

The README visuals under `assets/` are intentionally small, curated presentation assets and are safe to keep with the repository.

Before pushing, verify that no dataset/database files are tracked:

```bash
git ls-files | grep -E '\.(csv|tsv|parquet|feather|db|sqlite|sqlite3)$'
```

This command should return **nothing**.

---

# 🔍 Critical Interpretation Rules

## 1. Top 10 Is Not the Complete Netflix Catalog

A title absent from the Top 10 dataset is not equivalent to zero viewing.

```text
Not in Top 10
      ≠
Zero viewing
```

---

## 2. Country Is an Audience Market

Country observations represent the market in which the ranking was observed.

They are not production-country measurements.

```text
Audience market
      ≠
Production country
```

---

## 3. Missing Views Are Not Zero

Historical Netflix Top 10 records can have unavailable view metrics.

The pipeline preserves those values as missing.

```text
Missing
  ≠
Zero
```

---

## 4. TMDB Is External Metadata

TMDB enrichment is not Netflix audience data.

The current external metadata match rate is **51.92% at the entity level** in the audited build.

It should not be described as Netflix catalog coverage.

---

## 5. Prediction Is Not Causation

Forecasting and feature importance identify predictive relationships.

They do not establish causal effects.

```text
Feature is predictive
        ≠
Feature causes views
```

---

## 6. Survival Observations Are Censored

Titles still observed at the end of the available time window are right-censored.

Their eventual real-world lifetime may be longer than the observed lifetime.

---

## 7. Most Popular Is a Separate Measurement

The Most Popular all-time ranking is measured over the first 91 days and should not be interpreted as the same metric as weekly Top 10 performance.

---

## 8. H1 2026 Is a Separate Reference Source

The H1 2026 report is maintained as a separate reference dataset and is not silently treated as another weekly Top 10 fact table.

---

# ⚠️ Limitations

This project does not claim to measure:

- The complete Netflix catalog
- Total Netflix viewing across all Netflix titles
- Performance of titles that never appear in the Top 10
- Causal drivers of popularity
- Production-country effects from audience-market data
- Missing views as zero
- TMDB popularity as Netflix popularity

Additional limitations include:

### Top 10 Selection Bias

The data only represents titles meeting the Top 10 reporting criteria.

### Missing Metrics

Views and hours are not available uniformly across all records.

### Historical Availability

The observation period begins in July 2021.

### Metadata Coverage

External TMDB matching is incomplete.

Current audited entity coverage:

> **51.92%**

### Forecast Scope

The forecasting task predicts next-week views for already observed consecutive Top 10 entities.

It does not predict arbitrary future Top 10 entries.

### Causality

The project is observational.

Forecasting relationships and statistical associations should not be interpreted as causal effects.

### End-of-Window Censoring

Lifecycle measurements near the dataset boundary can be incomplete.

---

# 💼 Skills Demonstrated

## Data Analytics

- Exploratory Data Analysis
- KPI development
- Trend analysis
- Segmentation
- Market intelligence
- Lifecycle analysis
- Business-oriented interpretation

## SQL

- Analytical SQL
- Window functions
- Cohort analysis
- Concentration metrics
- HHI
- Data-quality queries
- Model diagnostics
- Drift analysis

## Python

- Pandas
- NumPy
- Scikit-learn
- Data validation
- Statistical analysis
- ETL/pipeline development

## Machine Learning

- Regression
- Forecasting
- Random Forest
- HistGradientBoosting
- Time-aware validation
- Permutation importance
- SHAP
- Forecast error analysis
- Model stability

## Data Engineering

- Source contracts
- Data normalization
- Analytical marts
- SQLite
- Provenance
- SHA-256 hashing
- Reproducible builds

## Visualization / BI

- Streamlit
- Matplotlib
- Plotly
- Executive KPI design
- Interactive drilldowns
- Analytical exports

## Engineering

- Pytest
- Automated validation
- Configuration
- Makefile workflows
- Git/GitHub
- Documentation
- Reproducibility

---

# 🎯 Business Questions This Project Supports

### Content

> Which titles perform consistently instead of relying on a single peak?

### Lifecycle

> How long do titles remain observable in the Top 10?

### Markets

> Which titles achieve broad market reach?

### Concentration

> Is a title's observed performance concentrated in a small number of markets?

### Momentum

> Which titles show unusual two-week acceleration?

### Forecasting

> Can recent Top 10 behavior help estimate next-week views?

### Data Quality

> Can analytical results be traced back to validated source data?

---

# 🖼️ Project Visuals

## Architecture

<p align="center">
<img src="assets/02_architecture.png" alt="Netflix analytics architecture" width="100%">
</p>

## Project Scale

<p align="center">
<img src="assets/03_project_kpis.png" alt="Netflix project scale" width="100%">
</p>

## Global Activity

<p align="center">
<img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="92%">
</p>

## Country Coverage

<p align="center">
<img src="assets/05_country_coverage.png" alt="Country coverage" width="92%">
</p>

## Forecast Benchmark

<p align="center">
<img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="92%">
</p>

## Data Quality

<p align="center">
<img src="assets/07_data_quality.png" alt="Data quality scorecard" width="92%">
</p>

---

# 📈 Additional Analytical Visuals

These visuals are generated from the project's analytical outputs and are intended to make the README show the breadth of the analysis rather than only the headline KPIs.

## Retention vs Churn

<p align="center">
<img src="assets/08_retention_churn.png" alt="Netflix Top 10 retention versus churn" width="92%">
</p>

Shows the observed weekly relationship between title retention and churn.

## Global Concentration

<p align="center">
<img src="assets/09_global_concentration.png" alt="Global Netflix content concentration" width="92%">
</p>

Tracks concentration across the leading observed titles.

## Breakout Titles

<p align="center">
<img src="assets/10_breakout_titles.png" alt="Netflix breakout titles" width="92%">
</p>

Highlights titles with strong observed two-week view acceleration.

## Country Similarity

<p align="center">
<img src="assets/11_country_similarity.png" alt="Netflix country market similarity" width="92%">
</p>

Shows the strongest observed similarities between audience markets.

## Statistical Evidence

<p align="center">
<img src="assets/12_statistical_effects.png" alt="Netflix statistical effect sizes" width="92%">
</p>

Summarizes reported statistical effect sizes from the project's inferential analysis.

## Forecast Model Feature Importance

<p align="center">
<img src="assets/13_model_feature_importance.png" alt="Forecast model feature importance" width="92%">
</p>

Compares permutation importance with mean absolute SHAP importance where available.

## Forecast Model Stability

<p align="center">
<img src="assets/14_model_stability.png" alt="Forecast model stability" width="92%">
</p>

Shows model performance across chronological validation cutoffs.

## Data Coverage Drift

<p align="center">
<img src="assets/15_data_drift.png" alt="Netflix data coverage drift" width="92%">
</p>

Shows how view coverage and unique observed entities change across periods.

## Cohort Lifecycle

<p align="center">
<img src="assets/16_cohort_median_views.png" alt="Netflix cohort lifecycle median views" width="92%">
</p>

Shows median observed views by cohort age.

---

# 🏁 Final Takeaway

**Netflix Content Intelligence v8.1 is an end-to-end analytics system, not just a visualization project.**

It combines:

```text
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

```text
Observed Top 10 performance
          ≠
Complete Netflix viewing
          ≠
Prediction
          ≠
Causation
```

That distinction is central to the design of the project.

---

# 📚 Official References

- Netflix Top 10: https://www.netflix.com/tudum/top10
- Netflix Global Weekly Dataset: https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv
- Netflix Country Weekly Dataset: https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv
- Netflix Most Popular: https://www.netflix.com/tudum/top10/most-popular
- Netflix H1 2026 Report: https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026

---

# 👤 Author

## Shubham Kumar Jha

Data Analytics • Business Analytics • Data Science • Scientific Data Analysis

I build data-driven projects combining:

- Analytics
- Statistics
- SQL
- Python
- Machine Learning
- Visualization
- Scientific analysis
- Business intelligence

---

# ⭐ If You Find This Project Useful

If this project is useful for learning, portfolio development, analytics engineering, or Netflix/content intelligence research:

- ⭐ Star the repository
- 🍴 Fork it
- 🐛 Open an issue
- 💡 Suggest an improvement
- 🔬 Explore the analytical methodology
- 📊 Reproduce the results

---

# 📜 Disclaimer

This project is an independent analytical project and is **not affiliated with, sponsored by, or endorsed by Netflix**.

Netflix and related trademarks belong to their respective owners.

The project uses publicly available Netflix Top 10 data for analytical and educational purposes.

---

<div align="center">

# 🎬 Netflix Content Intelligence v8.1

### Analyze • Validate • Explain • Forecast

**Python · SQL · Statistics · Machine Learning · Streamlit**

</div>
