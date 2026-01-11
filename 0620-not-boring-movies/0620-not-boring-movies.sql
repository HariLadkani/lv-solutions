# Write your MySQL query statement below
/*
id(PK) | movie | description | rating
1        avengers  sci-fi      9.85

id%2!=0 AND description != "boring" 
ORDER BY rating DESC

*/
SELECT
*
FROM Cinema
WHERE id%2 != 0 AND description != 'boring'
ORDER BY rating DESC; 