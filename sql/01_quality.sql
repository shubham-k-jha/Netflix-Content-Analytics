SELECT COUNT(*) AS rows, COUNT(DISTINCT week || '|' || category || '|' || weekly_rank) AS distinct_grain, SUM(CASE WHEN weekly_views IS NULL THEN 1 ELSE 0 END) AS missing_views FROM global_weekly;
