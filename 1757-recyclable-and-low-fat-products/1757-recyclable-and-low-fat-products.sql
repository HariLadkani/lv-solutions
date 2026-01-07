# Write your MySQL query statement below
#product_id : primary key
#low_fats: 'Y' or "N"
#recyclable: "Y" or "N"
SELECT 
product_id
FROM 
Products
WHERE 
low_fats = "Y" AND recyclable = "Y";
