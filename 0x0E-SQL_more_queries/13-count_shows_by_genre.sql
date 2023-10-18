-- Use the hbtn_0d_tvshows database
USE hbtn_0d_tvshows;

-- List all genres and the number of shows linked to each
SELECT genre AS 'genre', COUNT(*) AS 'number_of_shows'
FROM tv_show_genres
GROUP BY genre
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
