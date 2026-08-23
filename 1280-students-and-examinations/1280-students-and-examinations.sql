/*
each student takes every course from subjects table

goal:
    number of times each student attended each exam

ORDER BY student_id, subject_name

first group by on exam table on student_id and subject_name and count

cross join students table and subjects

then left join cross joined table with grouped exam table to fetch counts.

Null be shown as 0

| student_id | student_name | subject_name | attended_exams |
| ---------- | ------------ | ------------ | -------------- |
| 13         | John         | Programming  | 1              |
| 13         | John         | Physics      | 1              |
| 13         | John         | Math         | 1              |


| student_id | student_name | subject_name | attended_exams |



*/
SELECT 
    s.student_id,
    s.student_name,
    sub.subject_name,
    COALESCE(t.attended_exams, 0) AS attended_exams
FROM Students AS s
CROSS JOIN Subjects AS sub
LEFT JOIN 
    (SELECT 
        e.student_id,
        e.subject_name,
        COUNT(*) AS attended_exams
    FROM Examinations AS e
    GROUP BY e.student_id, e.subject_name) AS t
ON 
    t.student_id=s.student_id AND 
    t.subject_name=sub.subject_name

ORDER BY s.student_id ASC, sub.subject_name ASC


