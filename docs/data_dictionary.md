# Data dictionary

## Global weekly fact

| Field | Meaning |
|---|---|
| `week` | Sunday-ending Netflix Top 10 reporting week |
| `category` | Global Top 10 category: Films/TV × English/Non-English |
| `weekly_rank` | Rank 1–10 within category |
| `show_title` | Netflix published title label |
| `season_title` | Netflix published season/collection label when supplied |
| `weekly_hours_viewed` | Netflix published hours viewed for the week |
| `runtime` | Netflix runtime in hours |
| `weekly_views` | Netflix published views for the week; missing before published coverage |
| `cumulative_weeks_in_top_10` | Cumulative weeks in Top 10 |

## Country weekly fact

The country file contains the same ranking concept by audience market. It does **not** contain country-level views/hours. `country_name` and `country_iso2` describe the audience ranking geography, not production country.

## Most Popular

The current all-time Most Popular ranking supplied on 2026-10-05 is measured over each title’s first 91 days of viewing. It contains first-91-day hours/views for the top 10 in four categories.

## TMDB enrichment

`tmdb_data_legacy_2023.csv` is an older external reference dataset. It is used only for optional metadata enrichment. It is not a Netflix performance source. Current-title match coverage is expected to be materially lower than in the 2023 build and is reported explicitly.

## H1 2026 engagement report

The supplied H1 2026 report consists of two Netflix visual assets. Their 20 displayed rows were transcribed into `h1_2026_most_watched.csv` with the source period `2026 H1`. The images remain in `assets/` for visual verification.

## Identity keys

`title_family_key` links the same title/season across global and country sources. `entity_key` adds the source category, preventing same-name items in different global categories from being collapsed.
