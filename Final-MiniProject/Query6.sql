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