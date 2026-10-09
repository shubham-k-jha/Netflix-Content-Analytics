# Netflix Content Intelligence

**Global & Country Analytics · Content Lifecycle · Statistical Evidence · Forecasting · Machine Learning**

<p align="center">
  <img src="assets/01_hero_banner.png" alt="Netflix Content Intelligence" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Version-8.1-E50914?style=flat-square" alt="Version 8.1">
  <img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/SQL-25%20Analyses-336791?style=flat-square" alt="SQL analyses">
  <img src="https://img.shields.io/badge/Tests-37%2F37%20Reported-6C757D?style=flat-square" alt="Reported tests">
  <img src="https://img.shields.io/badge/Markets-94-111827?style=flat-square" alt="Audience markets">
</p>

<p align="center">
  A reproducible analytics system built from Netflix's published Top 10 data.
</p>

<p align="center">
  <a href="#project-at-a-glance">Overview</a> ·
  <a href="#visual-gallery">Visual Gallery</a> ·
  <a href="#forecasting-and-machine-learning">Forecasting</a> ·
  <a href="#architecture">Architecture</a> ·
  <a href="#getting-started">Get Started</a>
</p>

---

## Project at a glance

<table>
  <tr>
    <td align="center" width="25%">
      <h3>10,960</h3>
      Global weekly observations
    </td>
    <td align="center" width="25%">
      <h3>510,340</h3>
      Country weekly observations
    </td>
    <td align="center" width="25%">
      <h3>94</h3>
      Audience markets
    </td>
    <td align="center" width="25%">
      <h3>274 weeks</h3>
      2021-07-04 to 2026-09-27
    </td>
  </tr>
  <tr>
    <td align="center">
      <strong>25 / 25</strong><br>
      SQL analyses reported passed
    </td>
    <td align="center">
      <strong>37 / 37</strong><br>
      Tests reported passed
    </td>
    <td align="center">
      <strong>64 / 64</strong><br>
      Manifest hashes reported matched
    </td>
    <td align="center">
      <strong>13 pages</strong><br>
      Streamlit dashboard
    </td>
  </tr>
</table>

> **Metric provenance:** These figures are reported by the supplied project audit. They have not been freshly reproduced as part of this README repair.

> **Measurement boundary:** This project analyzes Netflix's published Top 10 measurements. It does not measure total viewing across the entire Netflix catalog. A title absent from the Top 10 must not be interpreted as having zero viewing.

## What this project does

Netflix Content Intelligence combines data ingestion, validation, normalization, SQL analytics, statistical testing, lifecycle measurement, market comparisons, forecasting, model diagnostics, and interactive reporting.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Business & Market Intelligence</h3>
      <ul>
        <li>Global weekly performance and rank trends</li>
        <li>Country-level audience-market comparisons</li>
        <li>Title retention, returns, and drop-off</li>
        <li>Cohorts, survival, and right-censoring</li>
        <li>Market concentration and breadth</li>
        <li>Breakout detection and two-week momentum</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Analytics Engineering & Modeling</h3>
      <ul>
        <li>Source contracts and data-quality validation</li>
        <li>25 SQL analysis modules</li>
        <li>Effect sizes, hypothesis tests, and false discovery rate control</li>
        <li>Chronological next-week views forecasting</li>
        <li>Permutation importance and SHAP when available</li>
        <li>Provenance manifests, hashes, tests, and SQLite</li>
      </ul>
    </td>
  </tr>
</table>

## Horizontal infographic: From source to insight

<table>
  <tr>
    <td align="center" width="16%">
      <h3>01</h3>
      📥<br><strong>INGEST</strong><br>
      <sub>Official Netflix TSVs</sub>
    </td>
    <td align="center" width="16%">
      <h3>02</h3>
      🧹<br><strong>VALIDATE</strong><br>
      <sub>Schema, grain, quality</sub>
    </td>
    <td align="center" width="16%">
      <h3>03</h3>
      🧱<br><strong>MODEL</strong><br>
      <sub>Normalized data marts</sub>
    </td>
    <td align="center" width="16%">
      <h3>04</h3>
      🔎<br><strong>ANALYZE</strong><br>
      <sub>SQL, statistics, lifecycle</sub>
    </td>
    <td align="center" width="16%">
      <h3>05</h3>
      🤖<br><strong>FORECAST</strong><br>
      <sub>Time-aware ML evaluation</sub>
    </td>
    <td align="center" width="16%">
      <h3>06</h3>
      📊<br><strong>DELIVER</strong><br>
      <sub>Dashboard, reports, tests</sub>
    </td>
  </tr>
</table>

## Horizontal infographic: Project footprint

<table>
  <tr>
    <td align="center" width="20%">
      <h3>10,960</h3>
      <sub>Global records</sub>
    </td>
    <td align="center" width="20%">
      <h3>510,340</h3>
      <sub>Country records</sub>
    </td>
    <td align="center" width="20%">
      <h3>94</h3>
      <sub>Markets</sub>
    </td>
    <td align="center" width="20%">
      <h3>25</h3>
      <sub>SQL modules</sub>
    </td>
    <td align="center" width="20%">
      <h3>37</h3>
      <sub>Reported tests</sub>
    </td>
  </tr>
</table>

*These figures are reported by the supplied project audit and have not been freshly rerun during this README update.*

---

## Visual gallery

The visuals follow the analytical story: system design and scale, performance, lifecycle and market behavior, statistical evidence, forecasting, and data quality.

Netflix H1 2026 report images are contextual references and remain separate from the weekly Top 10 data.

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>1. System architecture</h3>
      <img src="assets/02_architecture.png" alt="System architecture" width="100%">
      <p>The pipeline from official sources through validation, analytics, modeling, and reporting.</p>
    </td>
    <td width="50%" valign="top">
      <h3>2. Project scale</h3>
      <img src="assets/03_project_kpis.png" alt="Project KPIs" width="100%">
      <p>Dataset size, market coverage, SQL modules, and reported tests.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>3. Global weekly performance</h3>
      <img src="assets/04_global_weekly_views.png" alt="Global weekly views" width="100%">
      <p>Observed global Top 10 viewing activity over time.</p>
    </td>
    <td width="50%" valign="top">
      <h3>4. Country-market coverage</h3>
      <img src="assets/05_country_coverage.png" alt="Country-market coverage" width="100%">
      <p>Geographic breadth of audience-market observations, not production countries.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>5. Retention and churn</h3>
      <img src="assets/08_retention_churn.png" alt="Retention and churn" width="100%">
      <p>Continuation, disappearance, and return across weekly observations.</p>
    </td>
    <td width="50%" valign="top">
      <h3>6. Global concentration</h3>
      <img src="assets/09_global_concentration.png" alt="Global concentration" width="100%">
      <p>Whether observed performance is broadly distributed or concentrated.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>7. Breakout titles</h3>
      <img src="assets/10_breakout_titles.png" alt="Breakout titles" width="100%">
      <p>Titles showing unusual short-term acceleration under the project framework.</p>
    </td>
    <td width="50%" valign="top">
      <h3>8. Country similarity</h3>
      <img src="assets/11_country_similarity.png" alt="Country similarity" width="100%">
      <p>Similarities between markets based on observed title-performance patterns.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>9. Statistical effects</h3>
      <img src="assets/12_statistical_effects.png" alt="Statistical effects" width="100%">
      <p>Hypothesis-test evidence and effect sizes, with multiple-testing control where applicable.</p>
    </td>
    <td width="50%" valign="top">
      <h3>10. Forecast benchmark</h3>
      <img src="assets/06_forecast_benchmark.png" alt="Forecast benchmark" width="100%">
      <p>Chronological holdout results compared with a naive baseline.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>11. Feature importance</h3>
      <img src="assets/13_model_feature_importance.png" alt="Forecast feature importance" width="100%">
      <p>Predictors contributing to forecast performance. Importance is not causality.</p>
    </td>
    <td width="50%" valign="top">
      <h3>12. Model stability</h3>
      <img src="assets/14_model_stability.png" alt="Model stability" width="100%">
      <p>Variation in model behavior and errors across time or validation slices.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>13. Data coverage drift</h3>
      <img src="assets/15_data_drift.png" alt="Data coverage drift" width="100%">
      <p>Coverage changes that may affect interpretation of apparent trends.</p>
    </td>
    <td width="50%" valign="top">
      <h3>14. Cohort lifecycle</h3>
      <img src="assets/16_cohort_median_views.png" alt="Cohort lifecycle" width="100%">
      <p>Median observed views across lifecycle positions for title cohorts.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>15. Data quality</h3>
      <img src="assets/07_data_quality.png" alt="Data quality scorecard" width="100%">
      <p>Source grain, metric validity, coverage, title completeness, and metadata coverage.</p>
    </td>
    <td width="50%" valign="top">
      <h3>16. H1 2026: Top Movies</h3>
      <img src="assets/NFLX_H12026_EngagementReport_Top10Movies.png" alt="Netflix H1 2026 top movies" width="100%">
      <p>Netflix reference visual, separate from weekly Top 10 data.</p>
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <h3>17. H1 2026: Top Shows</h3>
      <img src="assets/NFLX_H12026_EngagementReport_Top10Shows.png" alt="Netflix H1 2026 top shows" width="100%">
      <p>Separate company-level reference, not a weekly Top 10 fact table.</p>
    </td>
    <td width="50%" valign="top">
      <h3>How to read the story</h3>
      <p>Sources → scale → performance → lifecycle and markets → statistical evidence → forecasting → stability and quality.</p>
    </td>
  </tr>
</table>

---

## Official data sources

| Source | Role |
|---|---|
| [Global Weekly Top 10 TSV](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv) | Global weekly title performance |
| [Country Weekly Top 10 TSV](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv) | Weekly performance by audience market |
| [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular) | Separate first-91-days ranking |
| [Netflix Top 10 portal](https://www.netflix.com/tudum/top10) | Published interface and methodology context |
| [What We Watched — H1 2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026) | Separate engagement-report reference |

Optional TMDB data is external reference metadata, not an authoritative Netflix-wide catalog or Netflix audience-performance data.

### Audited data scope

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
        |
        v
Raw TSV / CSV ingestion
        |
        v
Validation: schema, grain, dates, duplicates, missingness, metrics
        |
        v
Normalization: dates, entity keys, categories, content type
        |
        v
Analytical marts + SQLite
        |
        +-----------------------+
        |                       |
        v                       v
   SQL analytics          Statistical analysis
        |                       |
        +-----------+-----------+
                    |
                    v
Lifecycle, survival, concentration, market similarity, breakouts
                    |
                    v
Chronological forecasting, model interpretation, stability, drift
                    |
                    v
Reports, CSV exports, Streamlit dashboard
```

## Analytical framework

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Performance</h3>
      <ul>
        <li>Peak and average rank</li>
        <li>Peak views and hours</li>
        <li>Observed and elapsed longevity</li>
        <li>Rank volatility and performance segments</li>
      </ul>

      <h3>Lifecycle and survival</h3>
      <ul>
        <li>New, continuing, returning, and dropped titles</li>
        <li>Entry cohorts and weeks since entry</li>
        <li>Retention and survival curves</li>
        <li>Right-censoring at the observation boundary</li>
      </ul>

      <h3>Market intelligence</h3>
      <ul>
        <li>Country reach and title-market persistence</li>
        <li>Jaccard similarity between markets</li>
        <li>Top-1, Top-3, and Top-10 concentration</li>
        <li>Herfindahl-Hirschman Index (HHI)</li>
        <li>Global-versus-country comparisons</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Momentum and breakouts</h3>
      <ul>
        <li>Week-over-week movement and rank changes</li>
        <li>Two-week view acceleration</li>
        <li>New entries and cross-market expansion</li>
      </ul>

      <h3>Statistical evidence</h3>
      <ul>
        <li>Distribution and group comparisons</li>
        <li>Association analysis and effect sizes</li>
        <li>Hypothesis tests and p-values</li>
        <li>Benjamini-Hochberg false discovery rate control</li>
      </ul>

      <h3>Predictive analytics</h3>
      <ul>
        <li>Naive baseline, Ridge, Random Forest</li>
        <li>HistGradientBoosting</li>
        <li>Forecast error and chronological stability</li>
        <li>Permutation importance and SHAP when available</li>
      </ul>
    </td>
  </tr>
</table>

## Forecasting and machine learning

### Prediction task

> Estimate next-week views for entities with consecutive Top 10 observations.

This is **not** a model for predicting whether any arbitrary title will enter the Top 10. The current task focuses on entities already observed in consecutive weeks.

### Chronological validation

<table>
  <tr>
    <td align="center" width="33%">
      <h3>80 / 20</h3>
      <sub>Chronological holdout</sub>
    </td>
    <td align="center" width="33%">
      <h3>2026-01-25</h3>
      <sub>Reported cutoff week</sub>
    </td>
    <td align="center" width="33%">
      <h3>1,690 / 394</h3>
      <sub>Reported train / test rows</sub>
    </td>
  </tr>
</table>

The split preserves time order to reduce temporal leakage. Randomly mixing future observations into training would undermine this evaluation.

### Forecast benchmark

The following metrics are reported by the supplied project audit and have not been independently rerun here.

| Model | MAE | RMSE | R² | sMAPE | MAE improvement vs. naive |
|---|---:|---:|---:|---:|---:|
| Naive | 4,818,781.73 | 7,693,942.50 | -5.0073 | 0.7051 | 0% |
| Ridge | 1,306,746.39 | 2,481,223.14 | 0.3752 | 0.3047 | 72.88% |
| Random Forest | 772,008.52 | 1,811,793.36 | 0.6669 | 0.2018 | 83.98% |
| **HistGradientBoosting** | **752,565.16** | **1,748,406.59** | **0.6898** | **0.1974** | **84.38%** |

The supplied audit identifies HistGradientBoosting as the strongest non-naive model on this holdout, with a reported **84.38% MAE improvement** over the naive baseline. These values describe this specific task and split; they are not evidence of causation or a guarantee of future performance.

### Model diagnostics

- Feature and permutation importance
- SHAP explanations when available
- Error distributions and metric comparisons
- Stability across time or validation slices
- Data coverage drift

**Interpretation rule:** predictive importance describes how a model uses information. It does not establish that a feature causes viewership.

## SQL analytics

The project contains **25 SQL analysis modules**:

`quality` · `global_performance` · `country_performance` · `title_performance` · `lifecycle` · `retention` · `churn` · `momentum` · `breakouts` · `concentration` · `cohorts` · `market_intelligence` · `global_country_comparison` · `rank_analysis` · `views_analysis` · `hours_analysis` · `runtime_analysis` · `title_stability` · `market_breadth` · `content_mix` · `weekly_trends` · `entry_analysis` · `survival_analysis` · `forecast_features` · `model_performance_drift`

**Reported audit result:** 25/25 SQL analyses passed.

## Dashboard

The reported Streamlit dashboard contains 13 analytical pages.

<table>
  <tr>
    <td width="50%" valign="top">
      <ol>
        <li>Executive Overview</li>
        <li>Weekly Briefing</li>
        <li>Title Explorer</li>
        <li>Global & Cohorts</li>
        <li>Country Intelligence</li>
        <li>Entry / Retention / Churn</li>
        <li>Lifecycle & Concentration</li>
      </ol>
    </td>
    <td width="50%" valign="top">
      <ol start="8">
        <li>Breakouts & Momentum</li>
        <li>Forecasting & Model Stability</li>
        <li>Statistical Evidence</li>
        <li>Catalog & Metadata</li>
        <li>Most Popular & H1 2026</li>
        <li>Data Quality & Provenance</li>
      </ol>
    </td>
  </tr>
</table>

The supplied audit reports that the dashboard source and query contracts were validated. A live Streamlit HTTP smoke test was **not** completed in that audit environment because Streamlit was unavailable there.

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

The supplied validation summary reports:

<table>
  <tr>
    <td align="center" width="25%">
      <h3>37 / 37</h3>
      <sub>Tests reported passed</sub>
    </td>
    <td align="center" width="25%">
      <h3>25 / 25</h3>
      <sub>SQL analyses reported passed</sub>
    </td>
    <td align="center" width="25%">
      <h3>64 / 64</h3>
      <sub>Manifest hashes reported matched</sub>
    </td>
    <td align="center" width="25%">
      <h3>OK</h3>
      <sub>SQLite integrity reported</sub>
    </td>
  </tr>
</table>

Additional checks reported by the supplied audit include Python compilation, duplicate-grain checks, metric validation, and repository hygiene checks.

A pipeline run reportedly generates `reports/pipeline_run_manifest.json`, recording source, asset, and output information with SHA-256 hashes. Duplicate aliases are checked so alternate references to the same official source are not counted as unique facts.

> **Audit qualification:** These results come from the supplied project documentation. They have not been freshly rerun during this README rewrite. Do not claim that `make verify` has just succeeded unless it has been run to completion in the target environment.

## Getting started

### 1. Clone the repository

Replace the placeholders with your actual GitHub repository URL and folder name.

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
cd YOUR_REPOSITORY
```

### 2. Create and activate a virtual environment

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

For Linux, macOS, or another environment with `curl`:

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

The supplied audit also references Most Popular source aliases and optional legacy TMDB / H1 2026 assets. If the current pipeline requires those inputs, obtain them according to the repository documentation before attempting a complete rebuild.

### 5. Run the pipeline and checks

The following commands assume the corresponding Makefile targets exist:

```bash
make build
make validate
make analysis
make test
make verify
```

Run these commands locally and inspect their exit status. Do not treat the reported audit as proof that the current checkout passes.

### 6. Launch the dashboard

If the Makefile defines a `dashboard` target:

```bash
make dashboard
```

Equivalent command, if the entry point exists at this location:

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

The following is the documented project structure. Adjust it if the actual files in your repository differ.

```text
netflix_v8_1/
├── assets/
│   ├── 01_hero_banner.png
│   ├── 02_architecture.png
│   ├── 03_project_kpis.png
│   └── ... analytical figures
├── data/
│   ├── raw/                  # Local source files; do not commit
│   └── processed/            # Locally generated data; do not commit
├── dashboard/
│   └── app.py
├── docs/
│   ├── methodology.md
│   ├── limitations.md
│   ├── data_dictionary.md
│   ├── data_model.md
│   ├── lineage.md
│   └── schema_contract.json
├── reports/                  # Local generated outputs; do not commit
├── scripts/
│   └── run_pipeline.py
├── sql/                      # SQL analysis modules
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

Before pushing, inspect tracked data files:

```bash
git ls-files | grep -E '\.(csv|tsv|parquet|feather|db|sqlite|sqlite3)$'
```

This should return no tracked data/database files. If anything is returned, review it and remove unintended data files from tracking before pushing.

## Business questions this project supports

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Content & Lifecycle</h3>
      <ul>
        <li>Which titles perform consistently rather than relying on one peak?</li>
        <li>Which titles show unusual acceleration?</li>
        <li>How long do titles remain observable in the Top 10?</li>
        <li>Are lifecycle estimates incomplete because of right-censoring?</li>
      </ul>

      <h3>Markets & Portfolio</h3>
      <ul>
        <li>Which titles reach the most audience markets?</li>
        <li>Which markets show similar content patterns?</li>
        <li>Is observed engagement concentrated among a few titles?</li>
        <li>Where does a title perform strongly relative to its global results?</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Forecasting & Evidence</h3>
      <ul>
        <li>Can recent behavior estimate next-week views?</li>
        <li>Does a model beat a naive baseline?</li>
        <li>Are model errors stable over time?</li>
        <li>Are group differences statistically supported?</li>
      </ul>

      <h3>Trust & Reproducibility</h3>
      <ul>
        <li>Can data quality be checked before analysis?</li>
        <li>Are source aliases being double-counted?</li>
        <li>Can results be traced to input files?</li>
        <li>Can the analysis be rebuilt without committing source datasets?</li>
      </ul>
    </td>
  </tr>
</table>

## Critical interpretation rules

1. **Top 10 is not the full catalog.** A title absent from the dataset may still have viewers.
2. **Audience market is not production country.** Country records describe the market represented by the measurement.
3. **Missing is not zero.** Unavailable view metrics should remain missing rather than being silently converted to zero.
4. **TMDB is external metadata.** The reported entity-match coverage is 51.92%; this is not Netflix catalog coverage.
5. **Prediction is not causation.** Forecasting and feature importance do not establish causal effects.
6. **Observed lifecycle can be censored.** Titles still active at the end of the observation window may have longer real-world lifetimes.
7. **Most Popular is a different measurement.** Its first-91-days ranking is not interchangeable with weekly Top 10 performance.
8. **H1 2026 is a separate reference source.** It is not merged into weekly Top 10 fact tables.

## Limitations

This project does not claim to measure:

- Total Netflix viewing across the entire catalog
- Viewing for titles that never enter the Top 10
- The causes of a title's popularity
- Production-country effects from audience-market data
- Complete real-world lifetimes for right-censored titles
- Complete Netflix catalog coverage from TMDB matching

The dataset begins in July 2021, and view/runtime availability is not uniform across all records. Forecasting is limited to next-week views for entities already observed in consecutive Top 10 weeks. Results are observational and must be interpreted within these boundaries.

> **The central question:** What can we learn from Netflix's observed Top 10 measurements, and how reliably can those observations support analytical decisions?

## Skills demonstrated

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>Data Analytics</h3>
      <ul>
        <li>Exploratory analysis and KPI development</li>
        <li>Trend analysis, segmentation, and market intelligence</li>
        <li>Lifecycle analysis and business interpretation</li>
      </ul>

      <h3>SQL</h3>
      <ul>
        <li>Analytical queries and window functions</li>
        <li>Cohort, concentration, and survival analysis</li>
        <li>Data-quality queries and model diagnostics</li>
      </ul>

      <h3>Python</h3>
      <ul>
        <li>Pandas, NumPy, and Scikit-learn</li>
        <li>Statistical analysis</li>
        <li>Validation and pipeline development</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <h3>Machine Learning</h3>
      <ul>
        <li>Regression and forecasting</li>
        <li>Random Forest and HistGradientBoosting</li>
        <li>Time-aware validation</li>
        <li>Permutation importance and SHAP</li>
        <li>Forecast error and stability analysis</li>
      </ul>

      <h3>Data Engineering</h3>
      <ul>
        <li>Source contracts and normalization</li>
        <li>Analytical marts and SQLite</li>
        <li>Provenance and SHA-256 hashes</li>
        <li>Reproducible builds</li>
      </ul>

      <h3>Visualization & Engineering</h3>
      <ul>
        <li>Streamlit, Matplotlib, and Plotly</li>
        <li>Pytest, Makefile workflows, Git, and documentation</li>
      </ul>
    </td>
  </tr>
</table>

## Official references

- [Netflix Top 10 portal](https://www.netflix.com/tudum/top10)
- [Netflix Global Weekly Top 10 data](https://www.netflix.com/tudum/top10/data/all-weeks-global.tsv)
- [Netflix Country Weekly Top 10 data](https://www.netflix.com/tudum/top10/data/all-weeks-countries.tsv)
- [Netflix Most Popular](https://www.netflix.com/tudum/top10/most-popular)
- [Netflix: What We Watched — First Half of 2026](https://about.netflix.com/en/news/what-we-watched-the-first-half-of-2026)

## Author

**Shubham Kumar Jha**

Data Analytics · Business Analytics · Data Science · Scientific Data Analysis

I build analytical projects that combine Python, SQL, statistics, machine learning, visualization, and reproducible data workflows.

## Contribute

If this project is useful for learning, portfolio development, analytics engineering, or content intelligence research:

- Star the repository
- Fork it and explore the methodology
- Open an issue for bugs or improvements
- Reproduce the analytical outputs and report discrepancies

## Disclaimer

This is an independent analytical project and is **not affiliated with, sponsored by, or endorsed by Netflix**. Netflix and related trademarks belong to their respective owners. The project uses publicly available Netflix Top 10 data for analytical and educational purposes.

---

<p align="center">
  <strong>Netflix Content Intelligence v8.1</strong><br>
  <em>Analyze · Validate · Explain · Forecast</em><br>
  Python · SQL · Statistics · Machine Learning · Streamlit
</p>
