# Write your MySQL query statement below
/*
product_id | start_date | end_date | price
12            1-1-2022    1-1-2024    100
12            1-2-2024    1-11-2026   120
13            1-1-2022    1-1-2024    500

product_id | purchase_date | units
12           1-1-2022        100
12           1-1-2022        100
13           1-2-2023        100

Goal:
    avg selling price for each product_id
    2 decimal places
    return 0 if null sells
    avg selling = (price * units + price * units) / total units
*/
SELECT
product_id,
ROUND(COALESCE(SUM(total_price_per_order)/SUM(units),0), 2) AS average_price
FROM (
    SELECT 
        p.product_id,
        price,
        units,
        price * units AS total_price_per_order
    FROM Prices AS p
    LEFT JOIN UnitsSold AS u
    ON  u.purchase_date>=p.start_date AND
        u.purchase_date<=p.end_date AND 
        p.product_id = u.product_id
) AS t
GROUP BY product_id;

