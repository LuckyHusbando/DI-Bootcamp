--Exercise 1--

SELECT
    rating,
    COUNT(film_id) AS film_count
FROM
    film
GROUP BY
    rating;

SELECT
    title,
    rating,
    length,
    rental_rate
FROM
    film
WHERE
    (rating = 'G' OR rating = 'PG-13')
    AND length < 120
    AND rental_rate < 3.00
ORDER BY
    title ASC;

UPDATE
    customer
SET
    first_name = 'YourFirstName',
    last_name = 'YourLastName',
    email = 'youremail@example.com'
WHERE
    customer_id = 1; -- Or any other unique identifier    

-- First, find the address_id of the customer you updated
SELECT address_id FROM customer WHERE customer_id = 1;

-- Then, update the address in the address table using that ID
UPDATE
    address
SET
    address = 'Your New Address',
    phone = 'YourPhoneNumber',
    district = 'YourDistrict',
    city_id = 1 -- Replace with a valid city_id
WHERE
    address_id = (SELECT address_id FROM customer WHERE customer_id = 1);

--Exercise 2--

UPDATE students
SET birth_date = '1998-11-02'
WHERE first_name IN ('Lea', 'Marc') AND last_name = 'Benichou';

UPDATE students
SET last_name = 'Guez'
WHERE first_name = 'David' AND last_name = 'Grez';

DELETE FROM students
WHERE first_name = 'Lea' AND last_name = 'Benichou';

SELECT COUNT(*) FROM students;

SELECT COUNT(*)
FROM students
WHERE birth_date > '2000-01-01';

ALTER TABLE students
ADD COLUMN math_grade INTEGER;

UPDATE students SET math_grade = 80 WHERE id = 1;
UPDATE students SET math_grade = 90 WHERE id IN (2, 4);
UPDATE students SET math_grade = 40 WHERE id = 6;

SELECT COUNT(*) FROM students WHERE math_grade > 83;

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', (SELECT birth_date FROM students WHERE first_name = 'Omer' AND last_name = 'Simpson'), 70);

INSERT INTO students (first_name, last_name, birth_date, math_grade)
VALUES ('Omer', 'Simpson', (SELECT birth_date FROM students WHERE first_name = 'Omer' AND last_name = 'Simpson'), 85);

SELECT
    first_name,
    last_name,
    COUNT(math_grade) AS total_grade
FROM
    students
GROUP BY
    first_name, last_name;

SELECT SUM(math_grade) AS total_grades_sum
FROM students;

CREATE TABLE purchases (
    id SERIAL PRIMARY KEY,
    customer_id INTEGER REFERENCES customers(id),
    item_id INTEGER REFERENCES items(id),
    quantity_purchased INTEGER
);

INSERT INTO purchases (customer_id, item_id, quantity_purchased) VALUES
((SELECT id FROM customers WHERE first_name = 'Scott' AND last_name = 'Scott'),
(SELECT id FROM items WHERE item_name = 'fan'),
1),
((SELECT id FROM customers WHERE first_name = 'Melanie' AND last_name = 'Johnson'),
(SELECT id FROM items WHERE item_name = 'large desk'),
10),
((SELECT id FROM customers WHERE first_name = 'Greg' AND last_name = 'Jones'),
(SELECT id FROM items WHERE item_name = 'small desk'),
2);

SELECT * FROM purchases;

SELECT
    p.id,
    c.first_name,
    c.last_name,
    p.item_id,
    p.quantity_purchased
FROM
    purchases AS p
JOIN
    customers AS c ON p.customer_id = c.id;

SELECT * FROM purchases WHERE customer_id = 5;

SELECT *
FROM purchases
WHERE item_id IN (
    SELECT id FROM items WHERE item_name IN ('large desk', 'small desk')
);

SELECT
    c.first_name,
    c.last_name,
    i.item_name
FROM
    purchases AS p
JOIN
    customers AS c ON p.customer_id = c.id
JOIN
    items AS i ON p.item_id = i.id;

INSERT INTO purchases (customer_id, quantity_purchased) VALUES (1, 1);

