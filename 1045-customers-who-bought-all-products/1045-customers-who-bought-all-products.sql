# Write your MySQL query statement below
/*
Customer
    customer_id | product_key(fk)

Product
    product_key(pk)

goal:
    customer_id that have all the product_key found in product table

1 5
1 6
2 6

1 5 
1 6 
2 5
2 6

1 5 1
1 6 1
2 6 0

1 2
2 1
3 2



*/
SELECT
    customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product)
