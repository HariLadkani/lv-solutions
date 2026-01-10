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
machine_id,
ROUND(AVG(duration), 3) AS processing_time
FROM (
    SELECT 
    *,
    timestamp - LAG(timestamp) OVER (PARTITION BY Machine_id, process_id ORDER BY timestamp) AS duration
    FROM Activity) AS t
GROUP BY machine_id
;

