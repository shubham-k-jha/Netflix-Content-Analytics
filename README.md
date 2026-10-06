<div align="center">

# 🎬 Netflix Content Intelligence

### Source-Driven Netflix Top 10 Analytics • Global & Country Intelligence • Forecasting • Lifecycle Analysis

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

<p>
  <b>An end-to-end Netflix content analytics platform built from official Netflix Top 10 data.</b>
  <br>
  Python • SQL • Statistics • Machine Learning • Forecasting • Streamlit • Data Engineering
</p>

</div>

---

## 🚀 Project Overview

**Netflix Content Intelligence** is a production-style, source-driven analytics project that transforms Netflix's published Top 10 data into a complete analytical system.

The project covers:

- 🌍 Global weekly Top 10 performance
- 🗺️ Country-level market intelligence
- 🎬 Title-level performance analysis
- ⏳ Content lifecycle and survival analysis
- ⚡ Breakout and momentum detection
- 📊 Statistical analysis
- 🤖 Time-aware forecasting
- 🧠 Machine learning
- 🧮 SQL analytics
- 📈 Interactive Streamlit dashboard
- 🛡️ Data-quality validation
- 🔎 Data lineage and provenance
- 🧪 Automated testing
- 🔁 Reproducible data pipeline

> **Important:** Raw Netflix datasets are intentionally **not included in this repository** because they are large. The README provides official Netflix download links, and the complete analytical dataset is generated locally by the pipeline.

---

# 📊 Project at a Glance

<p align="center">
  <img src="assets/03_project_kpis.png" alt="Project KPIs" width="100%">
</p>

| Metric | Scope |
|---|---:|
| 🌍 Global weekly observations | **10,960** |
| 🗺️ Country weekly observations | **510,340** |
| 🌎 Markets | **94** |
| 📅 Weekly coverage | **274 weeks** |
| 🗓️ Coverage | **2021-07-04 → 2026-09-27** |
| 🏆 Most Popular titles | **40** |
| 🧮 SQL analyses | **25** |
| 🧪 Automated tests | **37 / 37** |
| 🗄️ Analytical database | **SQLite** |

---

# 🧭 Table of Contents

- [Project Overview](#-project-overview)
- [Project at a Glance](#-project-at-a-glance)
- [Why This Project](#-why-this-project)
- [Official Data Sources](#-official-data-sources)
- [Architecture](#-architecture)
- [Analytical Layers](#-analytical-layers)
- [Global Analytics](#-global-analytics)
- [Country Intelligence](#-country-intelligence)
- [Lifecycle & Survival](#-lifecycle--survival)
- [Breakout & Momentum](#-breakout--momentum)
- [Statistics](#-statistical-analysis)
- [Forecasting & ML](#-forecasting--machine-learning)
- [Dashboard](#-dashboard)
- [SQL Analytics](#-sql-analytics)
- [Data Quality](#-data-quality--provenance)
- [Repository Structure](#-repository-structure)
- [Installation](#-installation)
- [Download Data](#-download-the-data)
- [Run the Pipeline](#-run-the-pipeline)
- [Testing](#-testing)
- [Interpretation Rules](#-critical-interpretation-rules)
- [Limitations](#-limitations)
- [Skills Demonstrated](#-skills-demonstrated)

---

# 💡 Why This Project?

This project was designed to go beyond a typical Netflix visualization project.

Instead of taking a static dataset and creating charts, the system follows a complete data workflow:

```text
Official Netflix Sources
        ↓
Raw Data Ingestion
        ↓
Validation
        ↓
Normalization
        ↓
Analytical Data Modeling
        ↓
SQL + Statistics
        ↓
Lifecycle + Market Analysis
        ↓
Forecasting + ML
        ↓
Reports + SQLite
        ↓
Interactive Dashboard
