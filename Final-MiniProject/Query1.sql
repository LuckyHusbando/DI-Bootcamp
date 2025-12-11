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