# Write your MySQL query statement below

#unique columns:id, recordDate
SELECT 
w.id
FROM Weather AS w
INNER JOIN Weather AS w2
ON DATEDIFF(w.recordDate, w2.recordDate) = 1
WHERE w.temperature > w2.temperature;