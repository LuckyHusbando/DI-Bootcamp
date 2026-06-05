-- Create a new database named 'restaurant_db'
CREATE DATABASE restaurant_db;

-- Connect to the new database
\c restaurant_db;

-- Create the Menu_Items table
CREATE TABLE Menu_Items (
    item_id SERIAL PRIMARY KEY,
    item_name VARCHAR(30) NOT NULL,
    item_price SMALLINT DEFAULT 0
);

