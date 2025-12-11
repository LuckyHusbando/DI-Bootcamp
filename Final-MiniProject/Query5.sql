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