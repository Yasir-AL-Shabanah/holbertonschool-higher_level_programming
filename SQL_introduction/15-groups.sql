-- 15. Number by score
-- List number of records for each score in second_table
-- Ordered by number of records DESC
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
