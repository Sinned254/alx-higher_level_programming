-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Display the top 3 cities with the highest temperatures during July and August
SELECT city, MAX(temperature) AS max_temperature
FROM weather
WHERE MONTH(date) IN (7, 8)
GROUP BY city
ORDER BY max_temperature DESC
LIMIT 3;
