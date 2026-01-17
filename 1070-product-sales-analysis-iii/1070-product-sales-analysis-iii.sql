# Write your MySQL query statement below
/*
goal:
    all sales in first year of product sell

    for each product_id, rank on year and return where rank = 1
*/
WITH first_cte AS
(
    SELECT
        product_id,
        year,
        quantity,
        price,
        RANK() OVER (PARTITION BY product_id ORDER BY year)  AS ranking
    FROM Sales
)

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM first_cte 
WHERE ranking = 1;