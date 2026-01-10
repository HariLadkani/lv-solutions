# Write your MySQL query statement below

/*
goal:
    name, bonus
constraint:
    bonus < 1000 OR bonus IS NULL
*/

SELECT 
    e.name,
    b.bonus
FROM Employee AS e
LEFT JOIN Bonus AS b
ON e.empID = b.empId
WHERE b.bonus IS NULL OR b.bonus < 1000;
