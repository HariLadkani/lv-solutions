# Write your MySQL query statement below
#return product_name, year, price
#select from sales table year and price. LEFT JOIN proeuct table on product_id to fetch product_name

SELECT 
    p.product_name,
    s.year,
    s.price
FROM Sales AS s
LEFT JOIN
Product AS p
ON 
    p.product_id = s.product_id

