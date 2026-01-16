# Write your MySQL query statement below
/*
Delivery
    delivery_id (pk) | customer_id | order_date | customer_pref_delivery_date

immediate: customer_pref_delivery_date = order_date
scheduled: customer_pref_delivery_date != order_date

first order: earliest order date

goal:
    for each customer_id, find their first orders and return
    use case statements to find immediate or scheduled
    sum up immediate * 100 / total
    round 2 decimal
    

*/
WITH cte AS (
    SELECT 
        customer_id,
        order_date,
        customer_pref_delivery_date,
        MIN(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS first_order
    FROM Delivery
)

SELECT 
    ROUND(
        SUM(CASE
                WHEN order_date = first_order AND order_date = customer_pref_delivery_date THEN 1
                ELSE 0
            END
        ) * 100 / COUNT(DISTINCT customer_id,
        2
    )) AS immediate_percentage
FROM cte;