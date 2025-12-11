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