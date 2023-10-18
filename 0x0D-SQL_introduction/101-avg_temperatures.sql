-- Use the hbtn_0c_0 database
USE hbtn_0c_0;

-- Display average temperature (Fahrenheit) by city
SELECT city, AVG(temperature) AS avg_temperature
FROM weather
GROUP BY city
ORDER BY avg_temperature DESC;
