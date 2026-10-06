# Data lineage

`data/raw/all-weeks-global.tsv` → validation → `global_analytics.csv` → `global_weekly` → title mart / forecasting / SQL.

`data/raw/all-weeks-countries.tsv` → validation → `country_analytics.csv` → `country_weekly` → reach / concentration / similarity.

`data/raw/2026-10-05_global_alltime.tsv` → validation → `most_popular.csv` → `most_popular`.

`data/raw/tmdb_data_legacy_2023.csv` → deterministic title/type enrichment → `tmdb_metadata` + enrichment columns.

H1 2026 PNGs → manual transcription → `h1_2026_most_watched.csv` → `h1_2026_most_watched`.

Verified duplicate source files are retained for provenance and recorded in `source_registry`.
