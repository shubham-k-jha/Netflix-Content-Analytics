# Data model

```text
                         source_registry
                               |
          +--------------------+--------------------+
          |                    |                    |
   global_weekly        country_weekly        most_popular
          |                    |                    |
          +---------+----------+--------------------+
                    |
             entity_performance
                    |
          title_performance_mart
                    |
       +------------+-------------+
       |            |             |
   breakouts    survival     forecasting
       |
   statistics

   tmdb_metadata  ---> reference enrichment
   h1_2026_most_watched ---> separate engagement reference
```

The SQLite database is the analytical delivery layer. CSV outputs are retained for portability and inspection.
