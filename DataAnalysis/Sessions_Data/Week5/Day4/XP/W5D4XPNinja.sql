SELECT first_name, last_name, email
FROM customers
ORDER BY first_name ASC
LIMIT 2;

DELETE FROM purchases
WHERE customer_id = (SELECT id FROM customers WHERE first_name = 'Scott');

SELECT * FROM customers WHERE first_name = 'Scott';

SELECT
    c.first_name,
    c.last_name,
    p.quantity_purchased,
    p.item_id
FROM
    purchases AS p
LEFT JOIN
    customers AS c ON p.customer_id = c.id;

SELECT
    c.first_name,
    c.last_name,
    p.quantity_purchased,
    p.item_id
FROM
    purchases AS p
INNER JOIN
    customers AS c ON p.customer_id = c.id;