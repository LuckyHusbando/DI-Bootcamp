-- Create the Customer table
CREATE TABLE Customer (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

-- Create the Customer Profile table
CREATE TABLE CustomerProfile (
    id SERIAL PRIMARY KEY,
    isLoggedIn BOOLEAN DEFAULT FALSE,
    customer_id INTEGER UNIQUE REFERENCES Customer(id)
);

-- Insert customers
INSERT INTO Customer (first_name, last_name) VALUES
('John', 'Doe'),
('Jerome', 'Lalu'),
('Lea', 'Rive');

-- Insert customer profiles with subqueries
INSERT INTO CustomerProfile (isLoggedIn, customer_id) VALUES
(TRUE, (SELECT id FROM Customer WHERE first_name = 'John')),
(FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome'));

-- The first_name of the LoggedIn customers
SELECT c.first_name
FROM Customer AS c
INNER JOIN CustomerProfile AS cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = TRUE;

-- All customers first_name and isLoggedIn columns
SELECT c.first_name, cp.isLoggedIn
FROM Customer AS c
LEFT JOIN CustomerProfile AS cp ON c.id = cp.customer_id;

-- The number of customers that are not LoggedIn
SELECT COUNT(*)
FROM Customer AS c
LEFT JOIN CustomerProfile AS cp ON c.id = cp.customer_id
WHERE cp.isLoggedIn = FALSE OR cp.isLoggedIn IS NULL;

