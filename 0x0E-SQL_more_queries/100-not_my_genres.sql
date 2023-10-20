-- Find the genres linked to Dexter
SELECT genre_id
FROM tv_show_genres
WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter');

-- List all genres not linked to Dexter
SELECT tv_genres.name
FROM tv_genres
WHERE id NOT IN (
  SELECT genre_id
  FROM tv_show_genres
  WHERE show_id = (SELECT id FROM tv_shows WHERE title = 'Dexter')
)
