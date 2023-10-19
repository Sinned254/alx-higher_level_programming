-- List all shows with genres, including those without a genre
SELECT CONCAT(tv_shows.title, ' - ', IFNULL(tv_show_genres.genre_id, 'NULL')) AS 'Show and Genre'
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
