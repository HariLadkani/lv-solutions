# Write your MySQL query statement below
/*
Teacher
    teacher_id | subject_id | dept_id

goal:
    number of distinct subject_id for each teacher_id

*/
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id