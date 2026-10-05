--How to create a Table--

-- Create Table actors (
-- actor_id SERIAL Primary Key,
-- first_name VARCHAR(50) NOT NULL,
-- last_name VARCHAR(100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT
-- )

-- --How to insert Data into the Table
-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 5)

-- --How to retrieve data on the table

-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES ('Matt', 'Damon', '08/10/1970', 1),
-- ('Gal', 'Gadot', '06/12/1984', 2),
-- ('Meryl', 'Streep', '30/04/1935', 12);

SELECT first_name, number_oscars FROM actors WHERE last_name ILIKE '%mon%'


