
-- Bonus: Get customer details and payment info, ordered by the staff ID.
SELECT
    c.customer_id,
    c.first_name,
    c.last_name,
    p.amount,
    p.payment_date
FROM
    customer AS c
JOIN
    payment AS p 
ON 
    c.customer_id = p.customer_id
ORDER BY 
    p.staff_id;
