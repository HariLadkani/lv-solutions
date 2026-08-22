# Write your MySQL query statement below
SELECT 
    w1.id
FROM Weather AS w1
LEFT JOIN Weather AS w2
ON w1.recordDate - INTERVAL 1 DAY = w2.recordDate
WHERE w1.temperature > w2.temperature;

