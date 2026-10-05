--Query 1

SELECT
    COUNT(CASE WHEN T1.review_score = 5 THEN T1.order_id END) AS orders_jan_2018_5_star_count,
    COUNT(T1.order_id) AS total_orders_jan_2018_count,
    ROUND(
        (CAST(COUNT(CASE WHEN T1.review_score = 5 THEN T1.order_id END) AS REAL) * 100.0) / COUNT(T1.order_id), 
        2
    ) AS percentage_5_star
FROM
    orders AS T1
INNER JOIN
    order_reviews AS T2 ON T1.order_id = T2.order_id
WHERE
    STRFTIME('%Y-%m', T1.order_purchase_timestamp) = '2018-01';

--Query 2

SELECT
    STRFTIME('%Y', T1.order_purchase_timestamp) AS purchase_year,
    COUNT(DISTINCT T1.customer_id) AS unique_customers,
    COUNT(T1.order_id) AS total_orders,
    ROUND(SUM(T2.payment_value), 2) AS total_revenue
FROM
    orders AS T1
INNER JOIN
    order_payments AS T2 ON T1.order_id = T2.order_id
GROUP BY
    purchase_year
ORDER BY
    purchase_year;

--Query 3

WITH CustomerTotalSpent AS (
    SELECT
        T1.customer_unique_id,
        T1.order_id,
        SUM(T2.payment_value) AS order_value
    FROM
        customers AS T1
    INNER JOIN
        order_payments AS T2 ON T1.order_id = T2.order_id
    GROUP BY
        T1.customer_unique_id, T1.order_id
)
SELECT
    ROUND(AVG(order_value), 2) AS average_order_value_of_customers
FROM
    CustomerTotalSpent;

--Query 4

SELECT
    T1.customer_city,
    ROUND(SUM(T3.payment_value), 2) AS city_revenue
FROM
    customers AS T1
INNER JOIN
    orders AS T2 ON T1.customer_id = T2.customer_id
INNER JOIN
    order_payments AS T3 ON T2.order_id = T3.order_id
WHERE
    T2.order_status = 'delivered'
GROUP BY
    T1.customer_city
ORDER BY
    city_revenue DESC
LIMIT 5;

--Query 5

SELECT
    T1.customer_state,
    ROUND(SUM(T3.payment_value), 2) AS state_total_revenue
FROM
    customers AS T1
INNER JOIN
    orders AS T2 ON T1.customer_id = T2.customer_id
INNER JOIN
    order_payments AS T3 ON T2.order_id = T3.order_id
WHERE
    T2.order_status = 'delivered'
GROUP BY
    T1.customer_state
ORDER BY
    state_total_revenue DESC;

--Query 6

WITH SellerMetrics AS (
    SELECT
        T1.seller_id,
        COUNT(T1.order_item_id) AS total_goods_sold,
        ROUND(SUM(T1.price), 2) AS total_revenue,
        COUNT(DISTINCT T2.customer_id) AS unique_customers_served
    FROM
        order_items AS T1
    INNER JOIN
        orders AS T2 ON T1.order_id = T2.order_id
    GROUP BY
        T1.seller_id
),
SellerReviews AS (
    SELECT
        T1.seller_id,
        COUNT(T3.review_score) AS five_star_ratings
    FROM
        order_items AS T1
    INNER JOIN
        orders AS T2 ON T1.order_id = T2.order_id
    INNER JOIN
        order_reviews AS T3 ON T2.order_id = T3.order_id
    WHERE
        T3.review_score = 5
    GROUP BY
        T1.seller_id
)
SELECT
    T1.seller_id,
    T1.total_goods_sold,
    T1.total_revenue,
    T1.unique_customers_served,
    COALESCE(T2.five_star_ratings, 0) AS five_star_ratings,
    RANK() OVER (ORDER BY T1.total_goods_sold DESC) AS rank_goods_sold,
    RANK() OVER (ORDER BY T1.total_revenue DESC) AS rank_revenue,
    RANK() OVER (ORDER BY T1.unique_customers_served DESC) AS rank_customers_served,
    RANK() OVER (ORDER BY COALESCE(T2.five_star_ratings, 0) DESC) AS rank_5_star_ratings
FROM
    SellerMetrics AS T1
LEFT JOIN
    SellerReviews AS T2 ON T1.seller_id = T2.seller_id
ORDER BY
    rank_goods_sold
LIMIT 5;

--Query 7

SELECT
    T1.customer_state,
    COUNT(T2.order_id) AS total_orders,
    SUM(CASE WHEN T2.order_status = 'delivered' THEN 1 ELSE 0 END) AS delivered_orders,
    ROUND(
        (CAST(SUM(CASE WHEN T2.order_status = 'delivered' THEN 1 ELSE 0 END) AS REAL) * 100.0) / COUNT(T2.order_id),
        2
    ) AS delivery_success_rate_percent
FROM
    customers AS T1
INNER JOIN
    orders AS T2 ON T1.customer_id = T2.customer_id
GROUP BY
    T1.customer_state
ORDER BY
    delivery_success_rate_percent DESC;

--Query 8

WITH CategoryPaymentCount AS (
    SELECT
        T4.product_category_name_english,
        T3.payment_type,
        COUNT(T3.payment_type) AS payment_count
    FROM
        order_items AS T1
    INNER JOIN
        products AS T2 ON T1.product_id = T2.product_id
    INNER JOIN
        order_payments AS T3 ON T1.order_id = T3.order_id
    INNER JOIN
        product_category_translation AS T4 ON T2.product_category_name = T4.product_category_name
    GROUP BY
        T4.product_category_name_english, T3.payment_type
),
RankedPayments AS (
    SELECT
        product_category_name_english,
        payment_type,
        payment_count,
        ROW_NUMBER() OVER(PARTITION BY product_category_name_english ORDER BY payment_count DESC) AS rank_n
    FROM
        CategoryPaymentCount
)
SELECT
    product_category_name_english,
    payment_type AS most_preferred_payment
FROM
    RankedPayments
WHERE
    rank_n = 1
ORDER BY
    product_category_name_english;

--Query 9

CREATE TABLE IF NOT EXISTS city_coords AS
SELECT
    geolocation_city AS city,
    AVG(geolocation_lat) AS avg_lat,
    AVG(geolocation_lng) AS avg_lng
FROM
    geolocation
GROUP BY
    city;

-- Convert degrees to radians
CREATE TEMP TABLE IF NOT EXISTS temp_orders_with_coords AS
SELECT
    T3.order_id,
    T4.avg_lat AS customer_lat,
    T4.avg_lng AS customer_lng,
    T6.avg_lat AS seller_lat,
    T6.avg_lng AS seller_lng
FROM
    orders AS T3
INNER JOIN
    customers AS T1 ON T3.customer_id = T1.customer_id
INNER JOIN
    city_coords AS T4 ON T1.customer_city = T4.city
INNER JOIN
    order_items AS T5 ON T3.order_id = T5.order_id
INNER JOIN
    sellers AS T2 ON T5.seller_id = T2.seller_id
INNER JOIN
    city_coords AS T6 ON T2.seller_city = T6.city
LIMIT 1000; -- Limiting for performance/demo

-- Calculate Haversine Distance
SELECT
    T1.order_id,
    ROUND(
        6371 * ACOS(
            COS(RADIANS(T1.customer_lat)) * COS(RADIANS(T1.seller_lat)) *
            COS(RADIANS(T1.seller_lng) - RADIANS(T1.customer_lng)) +
            SIN(RADIANS(T1.customer_lat)) * SIN(RADIANS(T1.seller_lat))
        ),
        2
    ) AS distance_km
FROM
    temp_orders_with_coords AS T1
LIMIT 5;