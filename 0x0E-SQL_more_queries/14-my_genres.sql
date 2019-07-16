-- Select LEFT JOIN with Where clausule
-- Execute: cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
SELECT b.name
FROM tv_show_genres a
LEFT JOIN tv_genres b
ON a.genre_id = b.id
WHERE a.show_id = (SELECT id FROM tv_shows WHERE title = "Dexter")
ORDER BY 1 ASC;
