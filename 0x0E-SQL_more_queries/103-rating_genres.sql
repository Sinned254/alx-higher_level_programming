-- List all genres by their rating sum
SELECT tv_genres.name, SUM(rating) AS rating_sum
FROM tv_show_genres
JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
JOIN tv_show_ratings ON tv_show_genres.show_id = tv_show_ratings.show_id
GROUP BY tv_genres.name
ORDER BY rating_sum DESC;
