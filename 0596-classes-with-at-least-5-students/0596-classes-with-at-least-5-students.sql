# Write your MySQL query statement below
/*
class with COUNT(STUDENTS) >= 5
GOAl:
    RETURN CLASS
*/
SELECT
    class
FROM 
(
    SELECT
        class,
        COUNT(student) AS cnt
    FROM Courses
    GROUP BY class
) AS t
WHERE cnt >= 5;