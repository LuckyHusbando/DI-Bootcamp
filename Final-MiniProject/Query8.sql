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