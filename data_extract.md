#### List of actors born before 1980
``` SQL
SELECT name FROM main_actors_tbl
WHERE year_of_birth < 1980;
```
| name                  |
|-----------------------|
| Arnold Schwarzenegger |
| Signourey Weaver      |
| Christian Bale        |
| Leonardo DiCarpio     |
| Angelina Jolie        |
| Zoe Saldaña           |



#### How many movies did Nolan direct?
``` SQL
SELECT COUNT(title) FROM movies_tbl
	JOIN directors_tbl ON directors_tbl.id = movies_tbl.director_id 
WHERE directors_tbl.name LIKE "Christopher Nolan";
```

| COUNT(title) |
|--------------|
|            2 |



#### Among all the movies of James Cameron, how many were female actors?
``` SQL
SELECT COUNT(main_actors_tbl.name)
FROM movies_tbl
	JOIN movie_actors_tbl ON movies_tbl.id = movie_actors_tbl.movie_id
	JOIN main_actors_tbl ON main_actors_tbl.id = movie_actors_tbl.main_actor_id
	JOIN directors_tbl ON directors_tbl.id = movies_tbl.director_id 
WHERE directors_tbl.name LIKE "James Cameron" AND main_actors_tbl.sex LIKE "F";
```

| COUNT(main_actors_tbl.name) |
|-----------------------------|
|                           3 |



#### How many directors did Leonardo DiCaprio work with?

```SQL
SELECT COUNT(director_id)
FROM movies_tbl
	JOIN movie_actors_tbl ON movies_tbl.id = movie_actors_tbl.movie_id
	JOIN main_actors_tbl ON main_actors_tbl.id = movie_actors_tbl.main_actor_id
	JOIN directors_tbl ON directors_tbl.id = movies_tbl.director_id 
WHERE main_actors_tbl.name LIKE "Leonardo DiCaprio";
```

| COUNT(director_id) |
|--------------------|
|                  2 |



#### Who is the oldest actor?
``` SQL
SELECT name FROM main_actors_tbl
WHERE year_of_birth = (SELECT MIN(year_of_birth) from main_actors_tbl);
```

| name                  |
|-----------------------|
| Arnold Schwarzenegger |



#### What is the earliest movie of the oldest director?
```SQL
SELECT movies_tbl.title
FROM movies_tbl
	JOIN movie_actors_tbl ON movies_tbl.id = movie_actors_tbl.movie_id
	JOIN directors_tbl ON directors_tbl.id = movies_tbl.director_id 
WHERE directors_tbl.year_of_birth = (SELECT MIN(year_of_birth) from directors_tbl) 
AND movies_tbl.release_year = (SELECT MIN(release_year) from movies_tbl);
```

| title      |
|------------|
| Terminator |



#### What is the latest movie of the youngest actor?
```SQL
SELECT title
FROM movies_tbl
	JOIN movie_actors_tbl ON movies_tbl.id = movie_actors_tbl.movie_id
	JOIN main_actors_tbl ON main_actors_tbl.id = movie_actors_tbl.main_actor_id
WHERE main_actors_tbl.year_of_birth = (SELECT MAX(year_of_birth) from main_actors_tbl) 
AND movies_tbl.release_year = (SELECT MAX(release_year) from movies_tbl);
```

| title     |
|-----------|
| Cleopatra |
