-- Find the state_id for California in the states table
SET @california_state_id = (SELECT id FROM states WHERE name = 'California');

-- List all cities of California
SELECT id, name
FROM cities
WHERE state_id = @california_state_id
ORDER BY id ASC;
