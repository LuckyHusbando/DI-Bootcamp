SELECT
    f.title,
    f.description,
    f.rating
FROM
    film AS f
JOIN
    inventory AS i ON f.film_id = i.film_id
LEFT JOIN
    rental AS r ON i.inventory_id = r.inventory_id
WHERE
    f.rating IN ('G', 'PG') AND r.return_date IS NOT NULL
OR
    f.rating IN ('G', 'PG') AND r.rental_id IS NULL;

CREATE TABLE children_waitlist (
    waitlist_id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customer(customer_id),
    film_id INTEGER REFERENCES film(film_id)
);

INSERT INTO children_waitlist (customer_id, film_id) VALUES
(1, 10), -- A child is waiting for film ID 10
(2, 10), -- Another child is waiting for film ID 10
(3, 12); -- A third child is waiting for film ID 12

SELECT
    f.title,
    COUNT(cw.customer_id) AS waiting_count
FROM
    children_waitlist AS cw
JOIN
    film AS f ON cw.film_id = f.film_id
GROUP BY
    f.title
ORDER BY
    waiting_count DESC;

