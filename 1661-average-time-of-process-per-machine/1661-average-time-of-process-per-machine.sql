-- Write your PostgreSQL query statement below
SELECT
    a.machine_id,
    ROUND(AVG(CAST((b.timestamp - a.timestamp) AS numeric)), 3) AS processing_time
FROM Activity as a
LEFT JOIN Activity AS b
ON 
    a.machine_id = b.machine_id AND
    a.process_id = b.process_id AND 
    b.activity_type = 'end'
WHERE a.activity_type = 'start'
GROUP BY a.machine_id