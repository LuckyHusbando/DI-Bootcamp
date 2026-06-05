-- Select all columns from the “customer” table.
SELECT * FROM customer;

-- Display names (first_name, last_name) using an alias named “full_name”.
SELECT first_name || ' ' || last_name AS full_name
FROM customer;

-- Select all unique account creation dates from the “customer” table.
SELECT DISTINCT create_date
FROM customer;

-- Get all customer details from the "customer" table, ordered by first name in descending order.
SELECT *
FROM customer
ORDER BY first_name DESC;

-- Get film details in ascending order by rental rate.
SELECT film_id, title, description, release_year, rental_rate
FROM film
ORDER BY rental_rate ASC;

-- Get the address and phone number for all customers living in the Texas district.
SELECT address, phone
FROM address
WHERE district = 'Texas';

-- Retrieve movie details where the film ID is 15 or 150.
SELECT *
FROM film
WHERE film_id IN (15, 150);

-- Check for a specific movie in the database (e.g., 'Star Wars').
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title = 'Star Wars';

-- Get movie details for movies starting with the first two letters of a favorite movie.
SELECT film_id, title, description, length, rental_rate
FROM film
WHERE title LIKE 'St%';

-- Find the 10 cheapest movies.
SELECT *
FROM film
ORDER BY rental_rate ASC
LIMIT 10;

-- Find the next 10 cheapest movies.
SELECT *
FROM film
ORDER BY rental_rate ASC
OFFSET 10
LIMIT 10;

-- Bonus: Find the next 10 cheapest movies without using LIMIT.
-- This is not possible in standard SQL as OFFSET requires a LIMIT clause. However, some SQL dialects support it.

-- Join customer and payment tables to get customer names, payment amounts, and dates.
SELECT 
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM 
    customer AS c
JOIN 
    payment AS p 
ON 
    c.customer_id = p.customer_id
ORDER BY 
    c.customer_id ASC;

-- Get all movies that are not in inventory.
SELECT 
    f.film_id,
    f.title
FROM 
    film AS f
LEFT JOIN 
    inventory AS i 
ON 
    f.film_id = i.film_id
WHERE 
    i.film_id IS NULL;

-- Find which city is in which country.
SELECT 
    c.city,
    co.country
FROM 
    city AS c
JOIN 
    country AS co 
ON 
    c.country_id = co.country_id;