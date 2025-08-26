SELECT * FROM rental WHERE return_date IS NULL;

SELECT
    c.first_name,
    c.last_name
FROM
    customer AS c
JOIN
    rental AS r ON c.customer_id = r.customer_id
WHERE
    r.return_date IS NULL
GROUP BY
    c.customer_id;

SELECT
    f.title
FROM
    film AS f
JOIN
    film_category AS fc ON f.film_id = fc.film_id
JOIN
    category AS c ON fc.category_id = c.category_id
JOIN
    film_actor AS fa ON f.film_id = fa.film_id
JOIN
    actor AS a ON fa.actor_id = a.actor_id
WHERE
    c.name = 'Action'
    AND a.first_name = 'Joe'
    AND a.last_name = 'Swank';

CREATE VIEW film_details AS
SELECT
    f.title,
    f.description,
    c.name AS category_name,
    a.first_name,
    a.last_name
FROM
    film AS f
JOIN
    film_category AS fc ON f.film_id = fc.film_id
JOIN
    category AS c ON fc.category_id = c.category_id
JOIN
    film_actor AS fa ON f.film_id = fa.film_id
JOIN
    actor AS a ON fa.actor_id = a.actor_id;

SELECT
    title
FROM
    film_details
WHERE
    category_name = 'Action'
    AND first_name = 'Joe'
    AND last_name = 'Swank';

--Exercise 2--

SELECT
    COUNT(s.store_id) AS total_stores,
    city.city,
    country.country
FROM
    store AS s
JOIN
    address ON s.address_id = address.address_id
JOIN
    city ON address.city_id = city.city_id
JOIN
    country ON city.country_id = country.country_id
GROUP BY
    city.city, country.country;

SELECT
    s.store_id,
    SUM(f.length) AS total_minutes,
    SUM(f.length) / 60 AS total_hours,
    SUM(f.length) / 1440 AS total_days
FROM
    store AS s
JOIN
    inventory AS i ON s.store_id = i.store_id
JOIN
    film AS f ON i.film_id = f.film_id
WHERE
    i.inventory_id IN (
        SELECT inventory_id FROM rental WHERE return_date IS NOT NULL
    )
GROUP BY
    s.store_id;

SELECT
    c.first_name,
    c.last_name,
    city.city
FROM
    customer AS c
JOIN
    address ON c.address_id = address.address_id
JOIN
    city ON address.city_id = city.city_id
WHERE
    city.city_id IN (SELECT DISTINCT address.city_id FROM store JOIN address ON store.address_id = address.address_id);

SELECT
    c.first_name,
    c.last_name,
    country.country
FROM
    customer AS c
JOIN
    address ON c.address_id = address.address_id
JOIN
    city ON address.city_id = city.city_id
JOIN
    country ON city.country_id = country.country_id
WHERE
    country.country_id IN (SELECT DISTINCT
                            country.country_id
                        FROM
                            store
                        JOIN
                            address ON store.address_id = address.address_id
                        JOIN
                            city ON address.city_id = city.city_id
                        JOIN
                            country ON city.country_id = country.country_id);

SELECT
    SUM(f.length) AS total_safe_minutes,
    SUM(f.length) / 60 AS total_safe_hours,
    SUM(f.length) / 1440 AS total_safe_days
FROM
    film AS f
WHERE
    f.film_id NOT IN (
        SELECT fc.film_id
        FROM film_category AS fc
        JOIN category AS cat ON fc.category_id = cat.category_id
        WHERE cat.name = 'Horror'
    )
    AND f.title NOT ILIKE '%beast%'
    AND f.description NOT ILIKE '%beast%'
    AND f.title NOT ILIKE '%monster%'
    AND f.description NOT ILIKE '%monster%'
    AND f.title NOT ILIKE '%ghost%'
    AND f.description NOT ILIKE '%ghost%'
    AND f.title NOT ILIKE '%dead%'
    AND f.description NOT ILIKE '%dead%'
    AND f.title NOT ILIKE '%zombie%'
    AND f.description NOT ILIKE '%zombie%'
    AND f.title NOT ILIKE '%undead%'
    AND f.description NOT ILIKE '%undead%';

CREATE TABLE safe_film (
    -- other columns...
    title VARCHAR(255) CHECK (title NOT ILIKE '%zombie%' AND title NOT ILIKE '%ghost%')
);
