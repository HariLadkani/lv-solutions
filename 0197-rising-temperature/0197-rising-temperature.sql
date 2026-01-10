# Write your MySQL query statement below

#unique columns:id, recordDate
SELECT
    id
FROM (
    SELECT 
        *,
        LAG(temperature) OVER (ORDER BY recordDate) AS prev_day,
        LAG(recordDate) OVER (ORDER BY recordDate) AS prev_date 
    FROM Weather) As t
WHERE temperature > prev_day AND TIMESTAMPDIFF(day, prev_date, recordDate) = 1;