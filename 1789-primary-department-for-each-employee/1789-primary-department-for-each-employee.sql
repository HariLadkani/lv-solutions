# Write your MySQL query statement below
/*
When employee does not have a secondary department, flag = N

return employee with their primary department or only deparment 

steps:
    select ones with primary flag = y
    union
    select employees whose groupby returns count of 1
*/

SELECT 
    employee_id AS employee_id,
    department_id AS department_id
FROM Employee
WHERE primary_flag = 'Y'
UNION ALL
SELECT
    employee_id,
    MIN(department_id)
FROM Employee
GROUP BY employee_id
HAVING COUNT(*) = 1;
