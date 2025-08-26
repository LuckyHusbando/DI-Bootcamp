--Exercise 1--

SELECT * FROM language;

SELECT
    f.title,
    f.description,
    l.name AS language_name
FROM
    film AS f
INNER JOIN
    language AS l ON f.language_id = l.language_id;

SELECT
    f.title,
    f.description,
    l.name AS language_name
FROM
    film AS f
RIGHT JOIN
    language AS l ON f.language_id = l.language_id;

CREATE TABLE new_film (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

INSERT INTO new_film (name) VALUES
('The Matrix'),
('Inception'),
('Interstellar');

CREATE TABLE customer_review (
    review_id SERIAL PRIMARY KEY,
    film_id INTEGER REFERENCES new_film(id) ON DELETE CASCADE,
    language_id INTEGER REFERENCES language(language_id),
    title VARCHAR(255) NOT NULL,
    score INTEGER CHECK (score BETWEEN 1 AND 10),
    review_text TEXT,
    last_update TIMESTAMP NOT NULL DEFAULT NOW()
);

INSERT INTO customer_review (film_id, language_id, title, score, review_text) VALUES
((SELECT id FROM new_film WHERE name = 'The Matrix'), 1, 'Mind-Bending Classic!', 9, 'A truly great film that explores deep philosophical questions.'),
((SELECT id FROM new_film WHERE name = 'Inception'), 1, 'Dream Within A Dream', 10, 'One of the best thrillers of the decade, with an amazing plot and score.');

DELETE FROM new_film WHERE name = 'The Matrix';

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