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