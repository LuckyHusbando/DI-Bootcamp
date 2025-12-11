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