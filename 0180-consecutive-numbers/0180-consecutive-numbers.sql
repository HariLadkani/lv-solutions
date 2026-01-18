# Write your MySQL query statement below
WITH lag_cte AS
(
SELECT
    id,
    num,
    LAG(num, 1) OVER () AS last,
    LAG(num, 2) OVER () AS last_to_last
FROM Logs
) 

SELECT DISTINCT num AS ConsecutiveNums
FROM lag_cte 
WHERE num = last AND num = last_to_last; 