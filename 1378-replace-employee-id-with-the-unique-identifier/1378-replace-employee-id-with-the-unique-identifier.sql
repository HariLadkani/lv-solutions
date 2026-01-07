# Write your MySQL query statement below
# reutrn all names from Employees table LEFT JOIN other table on first table id = second table id

SELECT 
    unique_id,
    name 
FROM 
    Employees AS e
LEFT JOIN 
    EmployeeUNI AS u
ON e.id = u.id;

