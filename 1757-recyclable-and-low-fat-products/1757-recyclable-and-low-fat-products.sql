/*
output: Id where low_fats=y and recylable = y

*/
SELECT product_id
FROM Products 
WHERE low_fats = 'Y' AND recyclable = 'Y';
