# Catalog layer and provenance

## Important distinction

Netflix's published Top 10 files are **performance/ranking data**, not a complete current Netflix catalog. This project therefore does not fabricate a catalog universe from Top 10 observations.

v8 supports an optional historical/user-supplied `data/raw/netflix_titles.csv` snapshot. When supplied, it must contain at least:

- `show_id`
- `type`
- `title`
- `release_year`

Additional fields such as `director`, `cast`, `country`, `date_added`, `rating`, `duration`, `listed_in`, and `description` are retained when available.

The project labels this as `snapshot_only`; it is not silently treated as a current Netflix catalog.

## External reference metadata

The included TMDB file is a legacy external metadata enrichment source. It is useful for release dates, genres, production countries, runtime, popularity and other reference fields, but it is not Netflix audience measurement and is not a complete Netflix catalog.

## Performance bridge

When a catalog snapshot is supplied, v8 builds `catalog_performance_bridge.csv`, which links normalized catalog titles to Top 10 observations. A missing Top 10 match means **no observed Top 10 appearance in this dataset**, not zero viewing.
