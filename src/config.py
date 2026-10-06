from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw"
PROC = ROOT / "data" / "processed"
REPORTS = ROOT / "reports"
DOCS = ROOT / "docs"
ASSETS = ROOT / "assets"
LOGS = ROOT / "logs"
PIPELINE_VERSION = "8.1.0"

SOURCE_FILES = {
    "global_weekly": RAW / "all-weeks-global.tsv",
    "country_weekly": RAW / "all-weeks-countries.tsv",
    "global_weekly_snapshot": RAW / "2026-10-05_global_weekly.tsv",
    "global_alltime": RAW / "2026-10-05_global_alltime.tsv",
    "popular_weekly_snapshot": RAW / "most-popular_global_weekly.tsv",
    "popular_alltime_snapshot": RAW / "most-popular_global_alltime.tsv",
    "tmdb_legacy": RAW / "tmdb_data_legacy_2023.csv",
}

for p in (PROC, REPORTS, DOCS, LOGS):
    p.mkdir(parents=True, exist_ok=True)
