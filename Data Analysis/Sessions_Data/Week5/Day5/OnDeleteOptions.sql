-- CREATE TABLE cars_restrict(
-- car_id SERIAL PRIMARY KEY,
-- car_name varchar(100),
-- car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT ON UPDATE RESTRICT
-- );

-- DELETE FROM colors where name = 'yellow';
-- ERROR:  update or delete on table "colors" violates foreign key constraint -- "cars_car_color_fkey" on table "cars"
-- DETAIL:  Key (color_id)=(3) is still referenced from table "cars".

--On Delete or on Update Cascade - It will delete the row and the reference on the child will be null.

-- CREATE TABLE colors (
--     color_id SERIAL PRIMARY KEY,
--     name VARCHAR(50)
-- );

-- INSERT INTO colors (name) VALUES ('blue'), ('yellow'), ('pink');
-- SELECT * FROM colors

-- CREATE TABLE cars_restrict(
--     car_id SERIAL PRIMARY KEY,
--     car_name VARCHAR(100),
--     car_color INTEGER REFERENCES colors (color_id) ON DELETE RESTRICT ON UPDATE RESTRICT

-- INSERT INTO cars_restrict (car_name, car_color) VALUES ('Toyota', 1), ('Ford', 2), ('Honda', 3);

-- DELETE FROM colors WHERE name = 'blue'

-- CREATE TABLE cars_cascade (
--     car_id SERIAL PRIMARY KEY,
--     car_name VARCHAR(100),
--     car_color INTEGER REFERENCES colors (color_id) ON DELETE CASCADE ON UPDATE CASCADE
-- );

-- Update Colors set name = "grey" where name = 'yellow'
-- Select * From Cars_cascade

Select * from Colors

-- No Action, Cascade, & Set Null


