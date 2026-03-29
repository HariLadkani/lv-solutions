-- Write your PostgreSQL query statement below
SELECT
    MAX(e.name) AS name
FROM Employee AS e
LEFT JOIN Employee as f
ON 
    e.id = f.managerID

GROUP BY e.id
HAVING COUNT(e.id) >= 5