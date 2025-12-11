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