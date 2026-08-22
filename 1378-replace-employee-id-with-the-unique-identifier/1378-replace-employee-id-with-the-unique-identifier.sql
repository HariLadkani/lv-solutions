/*
goal:
    unique_id and namechoose 

left join on id in employees and employeeuni table
*/
SELECT 
    u.unique_id,
    e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u
ON e.id=u.id;


