# Write your MySQL query statement below
/*
8  1
8  2

*/
SELECT 
    MAX(number) AS num
FROM (
    SELECT
        num AS number
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(*) = 1
) AS t;
