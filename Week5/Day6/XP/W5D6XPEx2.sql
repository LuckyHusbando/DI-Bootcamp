--Exercise 2--

UPDATE film
SET language_id = (SELECT language_id FROM language WHERE name = 'French')
WHERE film_id IN (1, 2, 3);

DROP TABLE customer_review;

SELECT COUNT(*) FROM rental WHERE return_date IS NULL;

SELECT
    f.title,
    f.rental_rate
FROM
    rental AS r
JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
JOIN
    film AS f ON i.film_id = f.film_id
WHERE
    r.return_date IS NULL
ORDER BY
    f.rental_rate DESC
LIMIT 30;

SELECT
    f.title,
    f.description
FROM
    film AS f
JOIN
    film_actor AS fa ON f.film_id = fa.film_id
JOIN
    actor AS a ON fa.actor_id = a.actor_id
WHERE
    f.description ILIKE '%sumo wrestler%'
    AND a.first_name = 'Penelope'
    AND a.last_name = 'Monroe';

SELECT title, description
FROM film
WHERE length < 60 AND rating = 'R' AND description ILIKE '%documentary%';

SELECT
    f.title,
    f.description
FROM
    customer AS c
JOIN
    rental AS r ON c.customer_id = r.customer_id
JOIN
    payment AS p ON r.rental_id = p.rental_id
JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
JOIN
    film AS f ON i.film_id = f.film_id
WHERE
    c.first_name = 'Matthew'
    AND c.last_name = 'Mahan'
    AND p.amount > 4.00
    AND r.return_date BETWEEN '2005-07-28' AND '2005-08-01';

SELECT
    f.title,
    f.description,
    f.replacement_cost
FROM
    customer AS c
JOIN
    rental AS r ON c.customer_id = r.customer_id
JOIN
    inventory AS i ON r.inventory_id = i.inventory_id
JOIN
    film AS f ON i.film_id = f.film_id
WHERE
    c.first_name = 'Matthew'
    AND c.last_name = 'Mahan'
    AND (f.title ILIKE '%boat%' OR f.description ILIKE '%boat%')
ORDER BY
    f.replacement_cost DESC
LIMIT 1;