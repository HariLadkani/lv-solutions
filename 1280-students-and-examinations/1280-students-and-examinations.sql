# Write your MySQL query statement below

/*
each student_id takes all subjects in subject table

Examination:
    same student can take multiple exams of same subject

GOAL:
    number of times each student attended each exam
    order by student_id, subject_name

OUTPUT:
    student_id, student_name, subject_name, attended_exams

1. count duplicates of student_id, subject_name 
2. 
2. order by student_id, subject_name

1. group by student_id, subject_name and compute count
2. left join with students table and fetch student_name

*/
SELECT 
    s.student_id AS student_id,
    s.student_name AS student_name,
    subject.subject_name AS subject_name,
    CASE 
    WHEN agg.attended_exams THEN agg.attended_exams 
    ELSE 0
    END AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS subject
LEFT JOIN 
(
    SELECT 
        student_id AS agg_id,
        subject_name AS agg_name,
        COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) AS agg
ON s.student_id = agg.agg_id AND subject.subject_name = agg.agg_name
ORDER BY student_id, subject_name;
