# Write your MySQL query statement below
/*
Employees
    employee_id (pk) | name | reports_to | age

manager = employee_id that is in report_to for more than 1 employee

reports_to count age
9           2    39 

steps
group by on reports_to
compute avg_age and count
join with Employees to fetch name
*/
SELECT
    e2.employee_id,
    MIN(e2.name) AS name,
    COUNT(*) AS reports_count,
    ROUND(AVG(e1.age)) AS average_age
FROM Employees AS e1
INNER JOIN Employees AS e2
ON e1.reports_to=e2.employee_id
GROUP BY e1.reports_to
ORDER BY employee_id;