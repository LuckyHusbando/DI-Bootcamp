Select * from Movies

-- CREATE TABLE scenarios (
--   pk_movie_id INTEGER NOT NULL,
--   scenario_story TEXT NOT NULL,
--   PRIMARY KEY (pk_movie_id),
--   CONSTRAINT fk_movie_id FOREIGN KEY (pk_movie_id) REFERENCES movies (movie_id)

INSERT into movies(movie_title, released_date) VALUES 
('Good Will Hunting', '1997-12-02'),
('The Martian', '2015-09-11'),
('Oceans Twelve', '2004-12-10'),
('Up in the Air', '2009-09-5');

INSERT into scenarios(pk_movie_id, scenario_story) VALUES 
((SELECT movie_id FROM movies where movie_title = 'Up in the Air'),
'Ryan Bingham enjoys living out of a suitcase for his job, 
traveling around the country firing people, but finds that lifestyle 
threatened by the presence of a potential love interest, and a new hire.'),
((SELECT movie_id FROM movies where movie_title = 'The Martian'),
'In 2035, the crew of the Ares III mission to Mars is exploring 
Acidalia Planitia on Martian solar day (sol) 18 of their 31-sol expedition. ');

CREATE TABLE directors (
  director_id SERIAL,
  first_name VARCHAR(30) NOT NULL,
  last_name VARCHAR(30) NOT NULL,
  PRIMARY KEY (director_id)
);

/*
 one to many: A director directs many movies
*/

CREATE TABLE movies (
  movie_id SERIAL,
  movie_title VARCHAR(45) NOT NULL,
  released_date date NOT NULL,
  fk_director_id INTEGER NOT NULL,
  PRIMARY KEY (movie_id),
  FOREIGN KEY (fk_director_id) REFERENCES directors(director_id) ON DELETE CASCADE
);

INSERT  INTO DIRECTORS (FIRST_NAME, LAST_NAME)
VALUES ('Gus', 'Van Sant')
('Ridley', 'Scott')

INSERT into actors_movies(actor_id, movie_id, actor_role, is_lead_role) VALUES 
((SELECT actor_id FROM actors where first_name = 'George' AND last_name = 'Clooney' ), 
(SELECT movie_id FROM movies where movie_title = 'Up in the Air'), 'Ryan Bingham', TRUE),

((SELECT actor_id FROM actors where first_name = 'George' AND last_name = 'Clooney' ), 
(SELECT movie_id FROM movies where movie_title = 'Oceans Twelve'), 'Danny Ocean', FALSE),

((SELECT actor_id FROM actors where first_name = 'Matt' AND last_name = 'Damon' ),
(SELECT movie_id FROM movies where movie_title = 'Good Will Hunting'),'Will Hunting', TRUE);

