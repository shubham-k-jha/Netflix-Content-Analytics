SELECT content_type, COUNT(*) AS titles, AVG(longevity_weeks_observed) AS avg_observed_weeks, AVG(elapsed_weeks) AS avg_elapsed_weeks FROM entity_performance GROUP BY content_type;
