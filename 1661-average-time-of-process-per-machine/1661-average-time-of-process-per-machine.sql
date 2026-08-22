# Write your MySQL query statement below
/*
goal: avg time each machine_id takes to complete 
duration: end - start

output: machine_id, ROUND(processing_time, 3) 

1. for each (machine_id, process_id), 
    order by timestamp
    compute diff via lag function

2. group by machine_id 
3. sum grouped durations / count of process
*/
SELECT
    a1.machine_id,
    ROUND((SUM(a2.timestamp) - SUM(a1.timestamp)) / COUNT(a1.process_id), 3) AS processing_time
FROM Activity AS a1
LEFT JOIN Activity AS a2
ON 
    a1.machine_id=a2.machine_id AND
    a1.process_id=a2.process_id
WHERE 
    a1.activity_type='start' AND
    a2.activity_type = 'end'
GROUP BY a1.machine_id


