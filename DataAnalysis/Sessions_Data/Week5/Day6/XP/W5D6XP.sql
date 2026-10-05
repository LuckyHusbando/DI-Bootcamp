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