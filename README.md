<div align="center">

# 🎬 Netflix Content Intelligence

### Source-Driven Content Analytics • Global Top 10 Intelligence • Forecasting • Survival • Market Analytics

<p>
  <img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence" width="100%">
</p>

<p>
  <img src="https://img.shields.io/badge/Version-8.1-e50914?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQL-25%20Analyses-336791?style=for-the-badge" alt="SQL">
  <img src="https://img.shields.io/badge/Tests-37%2F37%20Passing-2ea44f?style=for-the-badge" alt="Tests">
  <img src="https://img.shields.io/badge/Markets-94-111827?style=for-the-badge" alt="Markets">
</p>

<p>
  <b>A full rebuild of Netflix Top 10 analytics from raw source data.</b><br>
  The project turns weekly global and country rankings into a reproducible analytical system covering
  content performance, market reach, lifecycle, momentum, concentration, forecasting, statistical evidence,
  data quality, and provenance.
</p>

</div>

---

## 🚀 Why this project is different

This is **not a static dashboard built on an old Kaggle snapshot**.

The pipeline starts from Netflix-published source files and rebuilds the analytical layer from scratch. It validates source contracts, protects against duplicate aliases, preserves structural missingness, creates entity-safe title keys, builds SQLite/CSV marts, executes 25 SQL analyses, runs statistical and forecasting workflows, and produces auditable reports.

> **Core principle:** the project analyzes what the source data actually measures — Netflix Top 10 performance — without pretending that Top 10 rankings represent the complete Netflix catalog or causal audience behavior.

---

## 📊 Project at a glance

<p align="center">
  <img src="assets/03_project_kpis.png" alt="Verified project scale" width="100%">
</p>

| Metric | Current scope |
|---|---:|
| 🌍 Global weekly observations | **10,960** |
| 🗺️ Country weekly observations | **510,340** |
| 🌎 Markets | **94** |
| 📅 Weekly coverage | **274 weeks** |
| 🗓️ Coverage period | **2021-07-04 → 2026-09-27** |
| 🏆 Current Most Popular ranking | **40 titles** |
| 🧮 SQL analyses | **25** |
| 🧪 Automated tests | **37 / 37** |
| 🗄️ Analytical database | **SQLite** |
| 📦 Pipeline | **Raw → Validate → Transform → Analyze → Report** |

---

# 🧭 Table of Contents

- [Project objective](#-project-objective)
- [Data sources](#-data-sources)
- [Architecture](#-architecture)
- [What is analyzed](#-what-is-analyzed)
- [Key analytical layers](#-key-analytical-layers)
- [Forecasting and ML](#-forecasting-and-ml)
- [Statistical analysis](#-statistical-analysis)
- [Dashboard](#-dashboard)
- [SQL analytics](#-sql-analytics)
- [Data quality and provenance](#-data-quality-and-provenance)
- [Visual results](#-visual-results)
- [Repository structure](#-repository-structure)
- [Run locally](#-run-locally)
- [Verification](#-verification)
- [Interpretation rules](#-interpretation-rules)
- [Limitations](#-limitations)
- [What this demonstrates](#-what-this-demonstrates)

---

# 🎯 Project objective

The goal is to answer practical content-business questions such as:

### Content performance
- Which titles consistently perform well?
- Which titles peak quickly versus sustain performance?
- How volatile are rankings?
- Which titles generate broad international reach?

### Lifecycle
- How long do titles remain in the Top 10?
- What distinguishes continuing, returning, new, and dropped titles?
- How does performance evolve after a title enters the ranking?
- Which entry cohorts show stronger persistence?

### Market intelligence
- Which countries have similar viewing patterns?
- Which titles travel across markets?
- Is performance concentrated in a small number of markets?
- How diversified is a title's country footprint?

### Momentum
- Which titles are accelerating?
- Which titles are breaking out over exact two-week intervals?
- How does rank movement relate to subsequent views?

### Forecasting
- Can next-week views be estimated for titles that remain in the Top 10?
- How much does a real model improve over a naive baseline?
- Which features are useful for prediction?

### Data reliability
- Are source files internally consistent?
- Are duplicate snapshots being double-counted?
- Where are views/runtime unavailable?
- Are generated outputs reproducible?

---

# 🗂️ Data sources

**The repository does not bundle the raw Netflix datasets.**  
To keep the GitHub repository lightweight and avoid redistributing Netflix source files, the pipeline expects you to download the source data from Netflix and place it under `data/raw/`.

### Official Netflix sources

| Dataset / source | Purpose | Official source |
|---|---|---|
| **All Weeks — Global** | Canonical global weekly Top 10 history | [Netflix Top 10 data](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv) |
| **All Weeks — Countries** | Canonical country weekly Top 10 history | [Netflix Top 10 country data](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv) |
| **Most Popular — Films & Shows** | Current all-time rankings measured over the first 91 days | [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular) |
| **Global Top 10** | Human-readable Top 10 interface and methodology | [Netflix Top 10](https://www.netflix.com/tudum/top10) |
| **What We Watched — H1 2026** | Six-month engagement reference and report assets | [Netflix H1 2026 report](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026) |

Netflix describes its weekly Top 10 as a view into what is popular on Netflix, while the *What We Watched* report is designed to capture broader viewing across the six-month period. citeturn0search0turn0search2

### Download the required weekly data

From the repository root:

```bash
mkdir -p data/raw

curl -L "https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
  -o data/raw/all-weeks-global.tsv

curl -L "https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
  -o data/raw/all-weeks-countries.tsv
```

Or with `wget`:

```bash
mkdir -p data/raw

wget -O data/raw/all-weeks-global.tsv \
  "https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv"

wget -O data/raw/all-weeks-countries.tsv \
  "https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv"
```

Then run:

```bash
make build
```

### Current Most Popular data

The project also uses Netflix's **Most Popular** ranking. This is a different analytical product from the weekly Top 10: the all-time ranking is measured over the **first 91 days** of a title's release window.

Use the official page to obtain the current ranking:

**[Netflix Most Popular — Films & Shows](https://www.netflix.com/tudum/top10/most-popular)**

### H1 2026 engagement report

The H1 2026 report is maintained separately from the weekly Top 10 pipeline:

**[Netflix — What We Watched: First Half of 2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026)**

The report covers viewing from January through June 2026 and is a broader engagement reference rather than a replacement for the weekly Top 10 dataset. citeturn0search0

### Optional external metadata

The repository can use the supplied legacy TMDB reference file for metadata enrichment. It is **optional** and is never treated as Netflix audience/performance data.

If you do not have the optional TMDB file, the core Netflix Top 10 analysis remains conceptually separate from that enrichment layer.

### Expected raw-data layout

```text
data/
└── raw/
    ├── all-weeks-global.tsv
    ├── all-weeks-countries.tsv
    ├── <current-most-popular-source>
    ├── <optional-tmdb-metadata>.csv
    └── <optional-h1-2026-assets>
```

### Important: duplicate snapshots

Some downloaded global snapshots may contain exactly the same underlying observations.

The pipeline retains source aliases only when needed for provenance and validates their equality. **Duplicate snapshots are never treated as additional facts.**

> **No raw Netflix data is committed to this repository. Download it directly from the official Netflix sources above.**

# 🏗️ Architecture

<p align="center">
  <img src="assets/02_architecture.png" alt="Netflix analytics architecture" width="100%">
</p>

The project follows a source-first architecture:

```text
Netflix published sources
        │
        ▼
┌──────────────────────┐
│ Raw ingestion        │
│ TSV / CSV / assets   │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Validation           │
│ schema / grain /     │
│ duplicates / ranges  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Normalization        │
│ dates / entities /   │
│ content types        │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Analytical marts     │
│ CSV + SQLite         │
└──────────┬───────────┘
           ├──────────────► SQL analytics
           ├──────────────► Statistics
           ├──────────────► Survival / cohorts
           ├──────────────► Forecasting / ML
           ├──────────────► Data-quality reports
           └──────────────► Streamlit dashboard
```

---

# 🔬 What is analyzed

## 1. Global Top 10

Weekly global title performance including:

- rank
- weekly views / hours where published
- weeks in Top 10
- peak performance
- movement over time
- title lifecycle

<p align="center">
  <img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="92%">
</p>

---

## 2. Country intelligence

The country dataset is treated as **audience-market information**.

It supports:

- country reach
- title-market persistence
- market concentration
- country similarity
- cross-market title performance
- country-level drilldowns

<p align="center">
  <img src="assets/05_country_coverage.png" alt="Country coverage" width="92%">
</p>

> **Important:** `country_name` means the market where the Top 10 ranking was observed. It does **not** mean the country where a title was produced.

---

# 🧠 Key analytical layers

### 📈 Performance intelligence

- Peak rank
- Average rank
- Peak views / hours
- Observed longevity
- Elapsed longevity
- Rank volatility
- Country reach
- Country concentration
- Performance segmentation

### ⏳ Lifecycle intelligence

- New entries
- Continuing titles
- Returning titles
- Dropped titles
- Entry cohorts
- Weeks-since-entry analysis
- Survival curves
- Right-censoring at the dataset boundary

### 🌍 Globalization intelligence

- Country reach
- Country persistence
- Jaccard country similarity
- Top-1 / Top-3 / Top-10 concentration
- HHI concentration
- Title-market drilldowns

### ⚡ Momentum intelligence

- Exact two-week acceleration
- Breakout detection
- Rank movement
- Weekly performance transitions

### 📊 Statistical evidence

- Effect sizes
- Association analysis
- Multiple-testing correction
- Benjamini–Hochberg FDR
- Uncertainty-aware reporting

---

# 🤖 Forecasting and ML

Machine learning is used only where the dataset supports a defensible target.

### Forecast target

**Next-week views**, conditional on an entity having consecutive Top 10 observations.

This avoids pretending that a Top-10-only dataset can reliably predict whether a completely unobserved Netflix title will enter the Top 10.

### Models

- Naive baseline
- Ridge Regression
- Random Forest
- HistGradientBoosting

### Validation

- Chronological train/test split
- Calendar-aware validation
- Multiple cutoff stability checks
- Fixed random seeds
- No random shuffling across time

### Evaluation

- MAE
- RMSE
- R²
- sMAPE
- Baseline improvement
- Forecast error analysis

<p align="center">
  <img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="92%">
</p>

### Interpretability

Where supported:

- permutation importance
- SHAP
- feature-level model diagnostics

> **Interpretation rule:** predictive importance is not causal impact.

---

# 📐 Statistical analysis

The statistical layer is designed to complement—not replace—the descriptive analysis.

It includes:

- group comparisons
- effect sizes
- association analysis
- uncertainty reporting
- multiple-testing correction
- false-discovery-rate control

The purpose is to distinguish:

> **“These groups look different”**

from:

> **“There is statistical evidence that the observed difference is unlikely to be explained by sampling variation alone.”**

And neither statement automatically implies causality.

---

# 🖥️ Dashboard

Run:

```bash
make dashboard
```

The Streamlit application is organized around decision-oriented pages:

| Page | Purpose |
|---|---|
| Executive Overview | KPIs and weekly business pulse |
| Title Explorer | Entity-safe title-level exploration |
| Global Trends | Global performance over time |
| Country Intelligence | Market-level analysis |
| Lifecycle & Survival | Persistence and cohort behavior |
| Breakouts & Momentum | Acceleration and movement |
| Forecasting & ML | Model performance and diagnostics |
| Statistical Evidence | Statistical findings |
| Most Popular & H1 2026 | Long-run/reference views |
| Data Quality & Provenance | Trust, lineage and source checks |

The dashboard also supports CSV exports for selected analytical views.

---

# 🧮 SQL analytics

The repository contains **25 executable SQL analyses** covering areas such as:

- data-quality checks
- title performance
- ranking movement
- lifecycle
- country intelligence
- concentration
- cohorts
- survival
- forecasting diagnostics
- model performance
- drift monitoring

SQL is executed against the rebuilt SQLite database rather than a manually edited static database.

---

# 🛡️ Data quality and provenance

Data quality is treated as a first-class analytical layer.

<p align="center">
  <img src="assets/07_data_quality.png" alt="Data quality scorecard" width="92%">
</p>

The pipeline validates:

- expected source row counts
- schema contracts
- date ranges
- unique analytical grain
- duplicate source aliases
- negative metrics
- missingness semantics
- generated analytical artifacts
- SQLite integrity
- SQL execution
- manifest integrity
- Python compilation
- supplied H1 2026 assets

Every build generates SHA-256 hashes through:

```text
reports/pipeline_run_manifest.json
```

This makes the output auditable and reproducible.

---

# 🧪 Testing

Run:

```bash
make test
```

The test suite covers:

- source contracts
- row counts and ranges
- grain uniqueness
- duplicate aliases
- missing-value semantics
- analytical output contracts
- model artifacts
- SQLite tables
- SQL execution
- provenance manifest
- negative metric checks
- H1 2026 assets
- Python compilation

Current audited package result:

**37 / 37 tests passing**

---

# 🔁 Reproducible pipeline

### 0. Download the raw data first

The repository intentionally does **not** contain the raw Netflix datasets.

Run the download commands in [Data sources](#-data-sources), then confirm:

```bash
ls -lh data/raw/
```

### 1. Install

```bash
python -m pip install -r requirements.txt
```

### 2. Build everything

```bash
make build
```

## Run tests

```bash
make test
```

## Full verification gate

```bash
make verify
```

## Or run the pipeline directly

```bash
python scripts/run_pipeline.py
```

The rebuild process:

```text
Clear generated layers
        ↓
Validate raw sources
        ↓
Validate duplicate aliases
        ↓
Normalize entities and dates
        ↓
Apply external metadata enrichment
        ↓
Build analytical marts
        ↓
Build SQLite database
        ↓
Run statistics + forecasting
        ↓
Execute SQL analyses
        ↓
Generate reports
        ↓
Write SHA-256 provenance manifest
```

---

# 📁 Repository structure

```text
netflix_v8_1/
│
├── assets/                         # README / report visuals
│
├── data/
│   ├── raw/                        # source files; never modified
│   └── processed/                  # generated analytical layer
│
├── dashboard/
│   └── app.py                      # Streamlit dashboard
│
├── docs/
│   ├── methodology.md
│   ├── limitations.md
│   ├── data_dictionary.md
│   ├── data_model.md
│   └── lineage.md
│
├── reports/                        # generated analytical reports
│
├── scripts/
│   └── run_pipeline.py
│
├── sql/                            # 25 executable SQL analyses
│
├── src/
│   ├── config.py
│   ├── validation.py
│   ├── pipeline.py
│   └── analysis.py
│
├── tests/
│
├── Makefile
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

# ⚠️ Interpretation rules

These rules are deliberately strict.

### 1. Top 10 ≠ full Netflix catalog

A title not present in the dataset is **not equivalent to zero viewing**.

### 2. Country ≠ production country

Country observations represent audience markets in the published ranking.

### 3. Missing views ≠ zero

Where Netflix does not publish a metric, the value remains missing.

### 4. TMDB ≠ Netflix audience data

TMDB is external reference metadata and is never treated as Netflix performance.

### 5. Prediction ≠ causation

A model can identify predictive relationships without proving that a feature causes performance.

### 6. Forecasting is conditional

The next-week forecasting task applies to entities with the required consecutive Top 10 observations.

### 7. Survival is censored

Titles still present at the dataset boundary are treated as right-censored rather than artificially assigned an ending date.

---

# 📌 Limitations

This project intentionally does **not** claim to measure:

- the complete Netflix catalog
- total Netflix viewing across all titles
- unobserved titles' performance
- causal drivers of popularity
- production-country effects from audience-market data
- missing views as zero
- TMDB popularity as Netflix popularity

The detailed methodological discussion is available in:

```text
docs/methodology.md
docs/limitations.md
```

---

# 💼 What this project demonstrates

This project is designed to demonstrate practical, job-relevant analytics engineering and data science skills:

### Data Analytics
- exploratory analysis
- KPI design
- business segmentation
- trend analysis
- market analysis

### SQL
- analytical queries
- window functions
- cohort analysis
- concentration metrics
- quality checks
- reproducible SQL execution

### Python
- Pandas
- NumPy
- statistical analysis
- Scikit-learn
- data validation
- pipeline engineering

### Data Engineering
- source contracts
- normalization
- analytical marts
- SQLite
- provenance
- deterministic builds

### Machine Learning
- time-aware validation
- forecasting
- model comparison
- feature importance
- error analysis

### BI / Product Thinking
- executive KPIs
- drilldowns
- decision-oriented dashboard design
- exportable analytical views

### Engineering quality
- automated tests
- reproducibility
- documentation
- data lineage
- integrity checks

---

# 🏁 Bottom line

**Netflix Content Intelligence v8.1 is an end-to-end analytics system—not just a visualization project.**

It combines:

```text
Real source data
      +
Data validation
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
Interpretability
      +
Dashboarding
      +
Testing
      +
Provenance
```

The result is a reproducible framework for turning Netflix's published Top 10 data into **decision-oriented content intelligence** while keeping the analytical claims aligned with what the underlying data can actually support.

---

<div align="center">

### 🎬 Built for analytical depth, reproducibility, and real-world decision making.

**Netflix Content Intelligence · v8.1**

</div>
