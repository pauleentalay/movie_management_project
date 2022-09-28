# create db
CREATE DATABASE movie_db;

# Show all databases;
SHOW DATABASES;

CREATE TABLE directors_tbl(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255), 
    year_of_birth int,
    PRIMARY KEY (id)
);

#shows information
DESRIBE directors_tbl;

#add entry
INSERT INTO directors_tbl VALUES(
    null,
    "James Cameron",
    1954
);

#Show all data inside TABLE
# SELECT
#FROM
#<WHERE>
SELECT * FROM directors_tbl;

## Create movie tables
CREATE TABLE movies_tbl(
    id int NOT NULL AUTO_INCREMENT,
    title varchar(255),
    release_year int,
    director_id int NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (director_id) REFERENCES directors_tbl(id)
);

INSERT INTO movies_tbl VALUES(
    null,
    "Titanic",
    1997,
    (SELECT id FROM directors_tbl WHERE name like "James Cameron")
);
;
INSERT INTO directors_tbl VALUES
(null, "James Cameron", 1954),
(null, "Christopher Nolan", 1970),
(null, "Patty Jenkins", 1971),   
(null, "Chloe Zhaos", 1982)
;

INSERT INTO movies_tbl VALUES
(null, "Wonder Woman", 2017, (SELECT id FROM directors_tbl WHERE name like "Patty Jenkins")),
(null, "Avatar", 2009, (SELECT id FROM directors_tbl WHERE name like "James Cameron")),
(null, "Aliens", 1986, (SELECT id FROM directors_tbl WHERE name like "James Cameron")),
(null, "Inception", 2010, (SELECT id FROM directors_tbl WHERE name like "Christopher Nolan")),
(null, "Terminator", 1984, (SELECT id FROM directors_tbl WHERE name like "James Cameron")),
(null, "Cleopatra", 2023, (SELECT id FROM directors_tbl WHERE name like "Patty Jenkins")),
(null, "Eternals", 2021, (SELECT id FROM directors_tbl WHERE name like "Chloe Zhaos")),
(null, "The Dark Knight", 2008, (SELECT id FROM directors_tbl WHERE name like "Christopher Nolan"))
;

# Selecting from multiple tables
SELECT movies_tbl.title, directors_tbl.name
FROM movies_tbl JOIN directors_tbl ON movies_tbl.director_id=directors_tbl.id
WHERE movies_tbl.title LIKE "Inception";

# Actors tables
CREATE TABLE main_actors_tbl(
    id int NOT NULL AUTO_INCREMENT,
    name varchar(255),
    year_of_birth int,
    sex varchar(1),
    PRIMARY KEY (ID)
);

INSERT INTO main_actors_tbl VALUES
(null, "Arnold Schwarzenegger", 1957, "M"),
(null, "Gal Gadot", 1985, "F"),
(null, "Signourey Weaver", 1949, "F"),
(null, "Christian Bale", 1974, "M"),
(null, "Leonardo DiCarpio", 1974, "M"),
(null, "Angelina Jolie", 1975, "F"),
(null, "Zoe Saldaña", 1978, "F"),
(null, "Gemma Chan", 1982, "F");


CREATE TABLE movie_actors_tbl(
    movie_id int NOT NULL,
    main_actor_id int NOT NULL,
    PRIMARY KEY (movie_id, main_actor_id),
    FOREIGN KEY (movie_id) REFERENCES movies_tbl(id),
    FOREIGN KEY (main_actor_id) REFERENCES main_actors_tbl(id)
);


INSERT INTO movie_actors_tbl VALUES(
(SELECT id FROM movies_tbl WHERE title like "Avatar"),
(SELECT id FROM main_actors_tbl WHERE name like "Zoe Saldaña")
);


INSERT INTO movie_actors_tbl VALUES
(
(SELECT id FROM movies_tbl WHERE title like "The Dark Knight"),
(SELECT id FROM main_actors_tbl WHERE name like "Christian Bale")
),
(
(SELECT id FROM movies_tbl WHERE title like "Inception"),
(SELECT id FROM main_actors_tbl WHERE name like "Leonardo DiCarpio")
),
(
(SELECT id FROM movies_tbl WHERE title like "Eternals"),
(SELECT id FROM main_actors_tbl WHERE name like "Angelina Jolie")    
),
INSERT INTO movie_actors_tbl VALUES
(
(SELECT id FROM movies_tbl WHERE title like "Aliens"),
(SELECT id FROM main_actors_tbl WHERE name like "Signourey Weaver")    
),
INSERT INTO movie_actors_tbl VALUES(
(SELECT id FROM movies_tbl WHERE title like "Cleopatra"),
(SELECT id FROM main_actors_tbl WHERE name like "Gal Gadot")    
),
(
(SELECT id FROM movies_tbl WHERE title like "Eternals"),
(SELECT id FROM main_actors_tbl WHERE name like "Gemma Chan")    
),
(
(SELECT id FROM movies_tbl WHERE title like "Titanic"),
(SELECT id FROM main_actors_tbl WHERE name like "Leonardo DiCarpio")    
),
(
(SELECT id FROM movies_tbl WHERE title like "Wonder Woman"),
(SELECT id FROM main_actors_tbl WHERE name like "Gal Gadot")    
),
(
(SELECT id FROM movies_tbl WHERE title like "Terminator"),
(SELECT id FROM main_actors_tbl WHERE name like "Arnold Schwarzenegger")    
),
(
(SELECT id FROM movies_tbl WHERE title like "Avatar"),
(SELECT id FROM main_actors_tbl WHERE name like "Signourey Weaver")    
);


# the above is the same as:

SELECT movies_tbl.title, main_actors_tbl.name
FROM movies_tbl
    JOIN movie_actors_tbl ON movies_tbl.id = movies_tbl.id
    JOIN main_actors_tbl ON main_actors_tbl.id = movie_actors_tbl.main_actor_id
WHERE movies_tbl.title LIKE "AVATAR";

DELETE FROM directors_tbl WHERE id=2;