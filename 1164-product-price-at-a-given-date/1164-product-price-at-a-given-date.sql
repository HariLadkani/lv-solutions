# Write your MySQL query statement below
/*
price of all products on 2019-08-16
initial price being 10

LESS THAN first value: use 10
change_date<2019-08-16<next_date: new_price
2019-08-16>=last_val: new_price
*/
WITH cte AS (
    SELECT 
    *,
    LEAD(change_date) OVER (PARTITION BY product_id ORDER BY change_date) AS next_date,
    FIRST_VALUE(change_date) OVER (PARTITION BY product_id ORDER BY change_date) AS first_date
    FROM 
    Products
) 

SELECT
    product_id,
    MAX((CASE
        WHEN '2019-08-16' < first_date THEN 10
        WHEN '2019-08-16' >= change_date AND '2019-08-16' < next_date THEN new_price
        WHEN '2019-08-16' >= change_date AND next_date IS NULL THEN new_price
    END)) AS price
FROM cte 
GROUP BY product_id