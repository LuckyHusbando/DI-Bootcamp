-- select * from movies

-- Joins in SQL

-------- Inner Join: See only related rows

-- Select actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- INNER JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-------- Left Join: See all columns, including null, from the right

-- Select actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- LEFT JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-------- Right Join: See all columns, including null, from the left

-- Select actors.first_name, actors.last_name, movies.movie_title
-- FROM actors
-- RIGHT JOIN movies
-- ON actors.actor_id = movies.actor_playing_id

-- Insert Into Movies (movies_title, movies_story, actor_playing_id)
-- Values ('The Lord of the Rings - the fellowship of the ring', 'the hobbits and pals piss off to Mordor,''')

-------- Full Join - See all columns from all tables

Create Table Countries (
country_id SERIAL Primary Key,
country_name Varchar(150) NOT NULL
);

Insert into countries (country_name)
Values ('Argentina'),
-- ('France')
-- ('Israel')
-- ('United States')
-- ('India')

---------It does the inner join on the ID so it matches the ID

Select actors.first_name, actors.last_name, 
From actors
Inner join Countries
