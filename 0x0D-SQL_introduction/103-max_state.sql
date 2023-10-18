-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Display the maximum temperature of each state ordered by state name
SELECT states.name AS state, MAX(temperature) AS max_temperature
FROM weather
INNER JOIN cities ON weather.city_id = cities.id
INNER JOIN states ON cities.state_id = states.id
GROUP BY state
ORDER BY state;
