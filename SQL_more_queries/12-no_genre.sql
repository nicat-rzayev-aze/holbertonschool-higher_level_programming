-- tabletabletable
SELECT tv_shows.title, tv_show_genres.genre_id 
FROM tv_shows 
RIGHT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id 
WHERE tv_shows.id IS NULL 
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC
