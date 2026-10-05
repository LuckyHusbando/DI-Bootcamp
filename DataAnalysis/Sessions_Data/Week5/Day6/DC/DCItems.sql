CREATE TABLE product_orders (
    order_id SERIAL PRIMARY KEY,
    order_date DATE NOT NULL,
    customer_name VARCHAR(100) NOT NULL
);

CREATE TABLE items (
    item_id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES product_orders(order_id),
    product_name VARCHAR(100) NOT NULL,
    price DECIMAL(10, 2) NOT NULL,
    quantity INTEGER NOT NULL
);

CREATE OR REPLACE FUNCTION get_total_order_price(p_order_id INTEGER)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    SELECT SUM(price * quantity) INTO total_price
    FROM items
    WHERE order_id = p_order_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;

CREATE TABLE users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

ALTER TABLE product_orders
ADD COLUMN user_id INTEGER REFERENCES users(user_id);

CREATE OR REPLACE FUNCTION get_user_order_price(p_order_id INTEGER, p_user_id INTEGER)
RETURNS DECIMAL(10, 2) AS $$
DECLARE
    total_price DECIMAL(10, 2);
BEGIN
    SELECT SUM(i.price * i.quantity) INTO total_price
    FROM items AS i
    JOIN product_orders AS po ON i.order_id = po.order_id
    WHERE i.order_id = p_order_id AND po.user_id = p_user_id;

    RETURN total_price;
END;
$$ LANGUAGE plpgsql;