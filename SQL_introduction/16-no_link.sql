-- 16. Say my name
-- List records from second_table where name is not empty
-- Show score and name ordered by score DESC
SELECT score, name FROM second_table
WHERE name IS NOT NULL
  AND name != ''
ORDER BY score DESC;
