<div align="center">

# Netflix Content Intelligence

### Global Performance · Content Lifecycle · Market Intelligence · Forecasting

<p>
  <img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence hero banner" width="100%">
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python 3.10+">
  <img src="https://img.shields.io/badge/SQL-25%20Analysis%20Modules-336791?style=for-the-badge" alt="25 SQL analysis modules">
  <img src="https://img.shields.io/badge/Markets-94-111827?style=for-the-badge" alt="94 audience markets">
  <img src="https://img.shields.io/badge/Tests-37%2F37%20Reported-2E8B57?style=for-the-badge" alt="37 of 37 tests reported passing">
</p>

**A reproducible analytics project built around Netflix's publicly available Top 10 data.**

[Explore the visuals](#visual-gallery) · [Understand the analysis](#analytical-framework) · [Forecast benchmark](#forecasting-and-machine-learning) · [Get started](#get-started)

</div>

---

## At a glance

<table>
  <tr>
    <td align="center" width="25%"><h2>10,960</h2><b>Global observations</b><br><sub>Weekly title records</sub></td>
    <td align="center" width="25%"><h2>510,340</h2><b>Country observations</b><br><sub>Weekly market records</sub></td>
    <td align="center" width="25%"><h2>94</h2><b>Audience markets</b><br><sub>Country-level coverage</sub></td>
    <td align="center" width="25%"><h2>274</h2><b>Weeks covered</b><br><sub>Jul 2021 – Sep 2026</sub></td>
  </tr>
  <tr>
    <td align="center"><b>25 / 25</b><br><sub>SQL analyses reported passing</sub></td>
    <td align="center"><b>37 / 37</b><br><sub>Automated tests reported passing</sub></td>
    <td align="center"><b>64 / 64</b><br><sub>Manifest hashes reported matching</sub></td>
    <td align="center"><b>13 pages</b><br><sub>Streamlit dashboard</sub></td>
  </tr>
</table>

> **Audit note:** Counts and test totals shown here come from the supplied project audit; they were not re-run as part of this README update.
>
> **Measurement boundary:** Netflix Top 10 data describes titles appearing in published rankings. It does **not** measure viewing across the entire Netflix catalogue. A title missing from the Top 10 must not be treated as having zero views.

## Contents

- [What this project does](#what-this-project-does)
- [Visual gallery](#visual-gallery)
- [Official data sources](#official-data-sources)
- [Architecture](#architecture)
- [Analytical framework](#analytical-framework)
- [Global performance](#global-performance)
- [Country intelligence](#country-intelligence)
- [Lifecycle and survival](#lifecycle-and-survival)
- [Breakouts and momentum](#breakouts-and-momentum)
- [Statistical analysis](#statistical-analysis)
- [Forecasting and machine learning](#forecasting-and-machine-learning)
- [SQL analytics](#sql-analytics)
- [Dashboard](#dashboard)
- [Data quality and provenance](#data-quality-and-provenance)
- [Get started](#get-started)
- [Repository structure](#repository-structure)
- [GitHub data policy](#github-data-policy)
- [Business questions](#business-questions-this-project-supports)
- [Interpretation rules](#critical-interpretation-rules)
- [Limitations](#limitations)
- [Skills demonstrated](#skills-demonstrated)
- [Official references](#official-references)

---

## What this project does

The project brings together data ingestion, data-quality checks, normalized analytical tables, SQL analysis, statistical testing, lifecycle measurement, market comparisons, forecasting, model diagnostics, and an interactive dashboard.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎬 Business & market intelligence</h3>
      <ul>
        <li>Global weekly performance and rank trends</li>
        <li>Country-level audience-market comparisons</li>
        <li>Title retention, returns, and drop-off</li>
        <li>Cohorts, survival analysis, and right-censoring</li>
        <li>Content concentration and market breadth</li>
        <li>Breakout detection and short-term momentum</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>🧪 Analytics engineering & modelling</h3>
      <ul>
        <li>Source contracts and data-quality validation</li>
        <li>25 SQL analysis modules</li>
        <li>Effect sizes, hypothesis tests, and FDR control</li>
        <li>Chronological next-week views forecasting</li>
        <li>Permutation importance and SHAP when available</li>
        <li>Provenance manifests, hashes, tests, and SQLite</li>
      </ul>
    </td>
  </tr>
</table>

## The workflow

<table>
  <tr>
    <td align="center" width="16%"><h3>01</h3>📥<br><b>INGEST</b><br><sub>Official Netflix TSVs</sub></td>
    <td align="center" width="16%"><h3>02</h3>🧹<br><b>VALIDATE</b><br><sub>Schema · grain · quality</sub></td>
    <td align="center" width="16%"><h3>03</h3>🧱<br><b>MODEL</b><br><sub>Normalized data marts</sub></td>
    <td align="center" width="16%"><h3>04</h3>🔎<br><b>ANALYZE</b><br><sub>SQL · statistics · lifecycle</sub></td>
    <td align="center" width="16%"><h3>05</h3>🤖<br><b>FORECAST</b><br><sub>Time-aware ML evaluation</sub></td>
    <td align="center" width="16%"><h3>06</h3>📊<br><b>DELIVER</b><br><sub>Dashboard · reports · tests</sub></td>
  </tr>
</table>

## Visual gallery

The gallery follows the analytical story: system design and project scale, performance, lifecycle and market behaviour, statistical evidence, forecasting, and data quality. The Netflix H1 2026 visuals are contextual references and are kept separate from the weekly Top 10 facts.

<table>
  <tr>
    <td width="50%" valign="top"><h3>1. System architecture</h3><img src="assets/02_architecture.png" alt="System architecture" width="100%"><sub>From official sources through validation, analytics, modelling, and reporting.</sub></td>
    <td width="50%" valign="top"><h3>2. Project at a glance</h3><img src="assets/03_project_kpis.png" alt="Project KPIs" width="100%"><sub>Dataset size, market coverage, SQL modules, and tests.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>3. Global weekly performance</h3><img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="100%"><sub>Observed global Top 10 viewing activity over time.</sub></td>
    <td valign="top"><h3>4. Country-market coverage</h3><img src="assets/05_country_coverage.png" alt="Country market coverage" width="100%"><sub>Geographic breadth of audience-market observations, not production countries.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>5. Retention and churn</h3><img src="assets/08_retention_churn.png" alt="Retention and churn" width="100%"><sub>Continuation, disappearance, and return across weekly observations.</sub></td>
    <td valign="top"><h3>6. Global concentration</h3><img src="assets/09_global_concentration.png" alt="Global concentration" width="100%"><sub>Whether observed performance is broadly distributed or concentrated.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>7. Breakout titles</h3><img src="assets/10_breakout_titles.png" alt="Breakout titles" width="100%"><sub>Titles with unusual short-term acceleration under the project framework.</sub></td>
    <td valign="top"><h3>8. Country similarity</h3><img src="assets/11_country_similarity.png" alt="Country similarity" width="100%"><sub>Market similarities based on observed title-performance patterns.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>9. Statistical effects</h3><img src="assets/12_statistical_effects.png" alt="Statistical effects" width="100%"><sub>Hypothesis-test evidence and effect sizes, with multiple-testing control where applicable.</sub></td>
    <td valign="top"><h3>10. Forecast benchmark</h3><img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="100%"><sub>Chronological holdout results compared with a naive baseline.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>11. Feature importance</h3><img src="assets/13_model_feature_importance.png" alt="Forecast feature importance" width="100%"><sub>Predictors contributing to forecast performance; importance is not causality.</sub></td>
    <td valign="top"><h3>12. Model stability</h3><img src="assets/14_model_stability.png" alt="Model stability" width="100%"><sub>Variation in model behaviour and errors across time or validation slices.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>13. Data coverage drift</h3><img src="assets/15_data_drift.png" alt="Data coverage drift" width="100%"><sub>Coverage changes that may affect interpretation of apparent trends.</sub></td>
    <td valign="top"><h3>14. Cohort lifecycle</h3><img src="assets/16_cohort_median_views.png" alt="Cohort lifecycle" width="100%"><sub>Median observed views across lifecycle positions for title cohorts.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>15. Data quality</h3><img src="assets/07_data_quality.png" alt="Data quality scorecard" width="100%"><sub>Source grain, metric validity, coverage, title completeness, and metadata coverage.</sub></td>
    <td valign="top"><h3>16. Netflix H1 2026 — Top Movies</h3><img src="assets/NFLX_H12026_EngagementReport_Top10Movies.png" alt="Netflix H1 2026 top movies" width="100%"><sub>Official Netflix reference visual, separate from weekly Top 10 data.</sub></td>
  </tr>
  <tr>
    <td valign="top"><h3>17. Netflix H1 2026 — Top Shows</h3><img src="assets/NFLX_H12026_EngagementReport_Top10Shows.png" alt="Netflix H1 2026 top shows" width="100%"><sub>Separate company-level reference, not a weekly Top 10 fact table.</sub></td>
    <td valign="middle"><h3>Follow the evidence</h3><p>Sources → scale → performance → lifecycle and markets → statistical evidence → forecasting → stability and quality.</p></td>
  </tr>
</table>

## Official data sources

| Source | What it provides |
|---|---|
| [Global Weekly Top 10 TSV](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv) | Global weekly title performance |
| [Country Weekly Top 10 TSV](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv) | Weekly performance by audience market |
| [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular) | Separate first-91-days ranking |
| [Netflix Top 10 portal](https://www.netflix.com/tudum/top10) | Published interface and methodology context |
| [What We Watched — H1 2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026) | Separate engagement-report reference |

Optional TMDB data is external reference metadata. It is not an authoritative Netflix-wide catalogue or a source of Netflix audience-performance data.

### Reported data scope

| Measure | Reported result |
|---|---:|
| Global weekly observations | 10,960 |
| Country weekly observations | 510,340 |
| Audience markets | 94 |
| Weekly coverage | 274 weeks |
| Coverage period | 2021-07-04 to 2026-09-27 |
| Current Most Popular records | 40 |
| Global source grain | 40 rows per week |
| Country source grain | 10 rows per category, week, and country |

## Architecture

```text
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
        ├────────────────────────┐
        ▼                        ▼
   SQL analytics          Statistical analysis
        └────────────┬───────────┘
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

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>📈 Performance</h3>
      <ul><li>Peak and average rank</li><li>Peak views and hours</li><li>Observed and elapsed longevity</li><li>Rank volatility and performance segments</li></ul>
      <h3>🔁 Lifecycle & survival</h3>
      <ul><li>New, continuing, returning, and dropped titles</li><li>Entry cohorts and weeks since entry</li><li>Retention and survival curves</li><li>Right-censoring at the observation boundary</li></ul>
      <h3>🌍 Market intelligence</h3>
      <ul><li>Country reach and title-market persistence</li><li>Jaccard similarity between markets</li><li>Top-1, Top-3, and Top-10 concentration</li><li>Herfindahl–Hirschman Index (HHI)</li><li>Global-versus-country comparisons</li></ul>
    </td>
    <td width="50%" valign="top">
      <h3>🚀 Momentum & breakouts</h3>
      <ul><li>Week-over-week movement and rank changes</li><li>Two-week view acceleration</li><li>New entries and cross-market expansion</li></ul>
      <h3>🧪 Statistical evidence</h3>
      <ul><li>Distribution and group comparisons</li><li>Association analysis and effect sizes</li><li>Hypothesis tests and p-values</li><li>Benjamini–Hochberg false discovery rate control</li></ul>
      <h3>🤖 Predictive analytics</h3>
      <ul><li>Naive baseline, Ridge, Random Forest, and HistGradientBoosting</li><li>Forecast error and chronological stability</li><li>Permutation importance and SHAP when available</li></ul>
    </td>
  </tr>
</table>

## Global performance

The global analysis describes title-level performance within Netflix's published weekly Top 10. It is designed to compare observed performance over time, not to estimate all viewing on Netflix.

- **Views and hours:** use the supplied metric when it is present; preserve missing values rather than converting them to zero.
- **Rank:** compare peak and average rank, while remembering that rank is ordinal and depends on the titles in the same weekly ranking.
- **Persistence:** distinguish the number of observed Top 10 weeks from a title's complete real-world lifetime.
- **Trend:** interpret week-to-week changes alongside changes in source coverage and metric availability.

## Country intelligence

Country-level records represent audience markets. They should not be interpreted as production-country labels. The project compares market reach, title persistence, market-level performance, and similarity in observed title patterns.

- Compare title presence and performance across markets using consistent time windows.
- Use market-breadth and persistence measures to distinguish broad reach from isolated appearances.
- Use Jaccard similarity for overlap in observed title sets, while recognizing that Top 10 cutoffs limit what can be observed.
- Compare global and country results as related but non-identical views of the published measurement.

## Lifecycle and survival

Lifecycle states describe observed transitions between weekly Top 10 snapshots: entry, continuation, disappearance, and return. These are measurement states, not evidence that people stopped watching a title.

Cohort analysis groups titles by an observed entry period and compares subsequent observed behaviour. Survival analysis must account for **right-censoring**: titles still present at the end of the observation window may remain in the Top 10 after the data ends.

## Breakouts and momentum

The breakout workflow flags titles with unusual short-term acceleration under the project's defined features. It combines recent view movement, rank changes, new entries, and cross-market expansion where those measurements are available.

A breakout flag is a screening signal, not a causal explanation or a guarantee of future performance. Compare flagged titles against the relevant baseline and inspect data coverage before drawing conclusions.

## Statistical analysis

The statistical workflow supports group and distribution comparisons, association analysis, hypothesis tests, and effect-size reporting. Where multiple hypotheses are tested, the project applies Benjamini–Hochberg false-discovery-rate control as described in its methodology.

Interpret results using both effect sizes and uncertainty—not p-values alone. Statistical association does not establish causation, and conclusions are limited by the observational nature and Top 10 selection of the data.

---

## Forecasting and machine learning

### Prediction task

> **Estimate next-week views for entities with consecutive Top 10 observations.**

This is **not** a model for predicting whether any arbitrary title will enter the Top 10. The task focuses on entities already observed in consecutive weeks.

### Chronological validation

<table>
  <tr>
    <td align="center" width="33%"><h3>80 / 20</h3><sub>Chronological holdout</sub></td>
    <td align="center" width="33%"><h3>2026-01-25</h3><sub>Cutoff week</sub></td>
    <td align="center" width="33%"><h3>1,690 / 394</h3><sub>Training / test rows</sub></td>
  </tr>
</table>

The split preserves time order to reduce temporal leakage. Randomly mixing future observations into training would undermine this evaluation.

### Forecast benchmark

| Model | MAE | RMSE | R² | sMAPE | MAE improvement vs. naive |
|---|---:|---:|---:|---:|---:|
| Naive | 4,818,781.73 | 7,693,942.50 | -5.0073 | 0.7051 | 0% |
| Ridge | 1,306,746.39 | 2,481,223.14 | 0.3752 | 0.3047 | 72.88% |
| Random Forest | 772,008.52 | 1,811,793.36 | 0.6669 | 0.2018 | 83.98% |
| **HistGradientBoosting** | **752,565.16** | **1,748,406.59** | **0.6898** | **0.1974** | **84.38%** |

The supplied audit identifies HistGradientBoosting as the strongest non-naive model on this holdout, with an **84.38% MAE improvement over the naive baseline**. These results apply to this defined task and split; they do not establish causation or guarantee future performance.

### Model diagnostics

- Feature and permutation importance
- SHAP explanations when available
- Error distributions and metric comparisons
- Stability across time or validation slices
- Data coverage drift

> **Interpretation rule:** Predictive importance describes how a model uses information; it does not establish that a feature causes viewership.

## SQL analytics

The project contains **25 SQL analysis modules**:

`quality` · `global_performance` · `country_performance` · `title_performance` · `lifecycle` · `retention` · `churn` · `momentum` · `breakouts` · `concentration` · `cohorts` · `market_intelligence` · `global_country_comparison` · `rank_analysis` · `views_analysis` · `hours_analysis` · `runtime_analysis` · `title_stability` · `market_breadth` · `content_mix` · `weekly_trends` · `entry_analysis` · `survival_analysis` · `forecast_features` · `model_performance_drift`.

**Reported audit result:** 25/25 SQL analyses passed.

## Dashboard

The Streamlit dashboard is organized into 13 analytical pages.

<table>
  <tr>
    <td width="50%" valign="top">
      <ul>
        <li>Executive Overview</li>
        <li>Weekly Briefing</li>
        <li>Title Explorer</li>
        <li>Global & Cohorts</li>
        <li>Country Intelligence</li>
        <li>Entry / Retention / Churn</li>
        <li>Lifecycle & Concentration</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <ul>
        <li>Breakouts & Momentum</li>
        <li>Forecasting & Model Stability</li>
        <li>Statistical Evidence</li>
        <li>Catalog & Metadata</li>
        <li>Most Popular & H1 2026</li>
        <li>Data Quality & Provenance</li>
      </ul>
    </td>
  </tr>
</table>

The supplied audit reported the dashboard source and query contracts as validated. A live Streamlit HTTP smoke test was **not** completed in that audit environment because Streamlit was unavailable there.

## Data quality and provenance

Data validation is part of the analytical workflow, not an afterthought.

| Quality metric | Reported audit result |
|---|---:|
| Source-grain integrity | 100% |
| Global view coverage | 62.77% |
| Global runtime coverage | 62.77% |
| Global hours coverage | 100% |
| TMDB entity coverage | 51.92% |
| Metric validity | 100% |
| Title completeness | 100% |

<table>
  <tr>
    <td align="center" width="25%"><h3>37 / 37</h3><sub>Tests reported passing</sub></td>
    <td align="center" width="25%"><h3>25 / 25</h3><sub>SQL analyses reported passing</sub></td>
    <td align="center" width="25%"><h3>64 / 64</h3><sub>Manifest hashes reported matching</sub></td>
    <td align="center" width="25%"><h3>OK</h3><sub>SQLite integrity reported</sub></td>
  </tr>
</table>

Additional reported checks: Python compilation passed; no duplicate global or country grain was detected; and no negative metrics, hardcoded local paths, stale source references, TODO/FIXME markers, or cache files were found in the audited project.

A pipeline run generates `reports/pipeline_run_manifest.json`, recording source, asset, and output information with SHA-256 hashes. Duplicate aliases are checked so alternate references to the same official source are not counted as unique facts.

> **Audit qualification:** These are results reported by the supplied project documentation, not freshly re-run as part of this README rewrite. Do not claim that `make verify` has just succeeded unless it has been run to completion in the target environment.

## Get started

> The commands below reflect the supplied project documentation. The repository source was not available for execution during this README rewrite, so confirm that the referenced files and Makefile targets exist before running them.

### 1. Clone the repository

Replace the placeholders with the actual GitHub repository URL and folder name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create a virtual environment

**Linux / macOS**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Download the official weekly datasets

```bash
mkdir -p data/raw

curl -L \
  "https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv" \
  -o data/raw/all-weeks-global.tsv

curl -L \
  "https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv" \
  -o data/raw/all-weeks-countries.tsv
```

Inspect the downloaded files:

```bash
ls -lh data/raw/
```

The supplied audit also used Most Popular source aliases and optional TMDB / H1 2026 reference assets. If the current pipeline requires these inputs, obtain them from the sources and documentation referenced by the repository before attempting a complete rebuild.

### 5. Run the pipeline and checks

```bash
make build
make validate
make analysis
make test
make verify
```

The supplied Makefile description says `make verify` runs the pipeline and then the automated test suite. Run it locally and inspect the exit status before claiming fresh successful verification.

### 6. Launch the dashboard

```bash
make dashboard
```

Equivalent command:

```bash
python -m streamlit run dashboard/app.py
```

Open the local URL printed by Streamlit.

### Useful commands

| Command | Purpose |
|---|---|
| `make build` | Run the pipeline |
| `make validate` | Run validation |
| `make analysis` | Run analysis |
| `make test` | Run automated tests |
| `make dashboard` | Launch Streamlit |
| `make verify` | Rebuild, then run tests |
| `make clean` | Remove generated outputs according to the Makefile |

## Repository structure

```text
netflix-content-intelligence/
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
├── sql/                    # SQL analysis modules
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

Keep source data and generated analytical outputs out of version control. Curated README images under `assets/` can remain in the repository.

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

Before pushing, inspect tracked files:

```bash
git ls-files | grep -E '\.(csv|tsv|parquet|feather|db|sqlite|sqlite3)$'
```

This should return no tracked data/database files. If anything is returned, review and remove those files from tracking before pushing.

## Business questions this project supports

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🎬 Content & lifecycle</h3>
      <ul><li>Which titles perform consistently rather than relying on one peak?</li><li>Which titles show unusual acceleration?</li><li>How long do titles remain observable in the Top 10?</li><li>Are lifecycle estimates incomplete due to right-censoring?</li></ul>
      <h3>🌍 Markets & portfolio</h3>
      <ul><li>Which titles reach the most audience markets?</li><li>Which markets show similar content patterns?</li><li>Is observed engagement concentrated among a few titles?</li><li>Where does a title perform strongly relative to its global results?</li></ul>
    </td>
    <td width="50%" valign="top">
      <h3>📊 Forecasting & evidence</h3>
      <ul><li>Can recent behaviour estimate next-week views?</li><li>Does a model beat a naive baseline?</li><li>Are model errors stable over time?</li><li>Are group differences statistically supported?</li></ul>
      <h3>🔐 Trust & reproducibility</h3>
      <ul><li>Can data quality be checked before analysis?</li><li>Are source aliases being double-counted?</li><li>Can results be traced to input files?</li><li>Can analysis be rebuilt without committing source datasets?</li></ul>
    </td>
  </tr>
</table>

## Critical interpretation rules

1. **Top 10 is not the full catalogue.** A title absent from the dataset may still have viewers.
2. **Audience market is not production country.** Country records describe the market represented by the measurement.
3. **Missing is not zero.** Unavailable view metrics remain missing rather than being silently converted to zero.
4. **TMDB is external metadata.** The reported entity match coverage is 51.92%; this is not Netflix catalogue coverage.
5. **Prediction is not causation.** Forecasting and feature importance do not establish causal effects.
6. **Observed lifecycle can be censored.** Titles still active at the end of the observation window may have longer real-world lifetimes.
7. **Most Popular is a different measurement.** Its first-91-days ranking is not interchangeable with weekly Top 10 performance.
8. **H1 2026 is a separate reference source.** It is not merged into weekly Top 10 fact tables.

## Limitations

This project does not claim to measure:

- Total Netflix viewing across the entire catalogue
- Viewing for titles that never enter the Top 10
- The causes of a title's popularity
- Production-country effects from audience-market data
- Complete real-world lifetimes for right-censored titles
- Complete Netflix catalogue coverage from TMDB matching

The dataset begins in July 2021, and view/runtime availability is not uniform across all records. Forecasting is limited to next-week views for entities already observed in consecutive Top 10 weeks. Results are observational and must be interpreted within these boundaries.

> **The central question:** What can we learn from Netflix's observed Top 10 measurements, and how reliably can those observations support analytical decisions?

## Skills demonstrated

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>📊 Data analytics</h3>
      <ul><li>Exploratory analysis and KPI development</li><li>Trend analysis, segmentation, and market intelligence</li><li>Lifecycle analysis and business interpretation</li></ul>
      <h3>🗄️ SQL</h3>
      <ul><li>Analytical queries and window functions</li><li>Cohort, concentration, and survival analysis</li><li>Data-quality queries and model diagnostics</li></ul>
      <h3>🐍 Python</h3>
      <ul><li>Pandas, NumPy, and Scikit-learn</li><li>Statistical analysis</li><li>Validation and pipeline development</li></ul>
    </td>
    <td width="50%" valign="top">
      <h3>🤖 Machine learning</h3>
      <ul><li>Regression and forecasting</li><li>Random Forest and HistGradientBoosting</li><li>Time-aware validation, permutation importance, and SHAP</li><li>Forecast error and stability analysis</li></ul>
      <h3>⚙️ Data engineering</h3>
      <ul><li>Source contracts and normalization</li><li>Analytical marts and SQLite</li><li>Provenance, SHA-256 hashes, and reproducible builds</li></ul>
      <h3>📈 Visualization & engineering</h3>
      <ul><li>Streamlit, Matplotlib, and Plotly</li><li>Pytest, Makefile workflows, Git, and documentation</li></ul>
    </td>
  </tr>
</table>

## Official references

- [Netflix Top 10 portal](https://www.netflix.com/tudum/top10)
- [Netflix Global Weekly Top 10 data](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv)
- [Netflix Country Weekly Top 10 data](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv)
- [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular)
- [Netflix: What We Watched — First Half of 2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026)

## About the author

**Shubham Kumar Jha**  
Data Analytics · Business Analytics · Data Science · Scientific Data Analysis

I build analytical projects that combine Python, SQL, statistics, machine learning, visualization, and reproducible data workflows.

## Contribute

If this project is useful for learning, portfolio development, analytics engineering, or content-intelligence research:

- ⭐ Star the repository
- 🍴 Fork it and explore the methodology
- 🐛 Open an issue for bugs or improvements
- 🔬 Reproduce the analytical outputs and report discrepancies

## Disclaimer

This is an independent analytical project and is **not affiliated with, sponsored by, or endorsed by Netflix**. Netflix and related trademarks belong to their respective owners. The project uses publicly available Netflix Top 10 data for analytical and educational purposes.

---

<div align="center">

**Analyze · Validate · Explain · Forecast**

*Python · SQL · Statistics · Machine Learning · Streamlit*

</div>
