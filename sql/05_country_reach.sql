SELECT country_name, country_iso2, COUNT(DISTINCT entity_key) AS distinct_titles, AVG(weekly_rank) AS avg_rank FROM country_weekly GROUP BY country_name,country_iso2 ORDER BY distinct_titles DESC;
