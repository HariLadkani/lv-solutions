# Write your MySQL query statement below
/*
confirmation rate = ROUND(# of confirmed / total, 2)

1. WE NEED signups table with user_id
2. we need confirmations table
3. group by on user_id, time_stamp
4. AVG(case where action is confirmed)
*/

SELECT
s.user_id,
ROUND(
    AVG(
        CASE WHEN c.action = 'confirmed' THEN 1
        ELSE 0 
        END
    ), 
2) AS confirmation_rate
FROM Signups AS s
LEFT JOIN Confirmations AS c
ON s.user_id = c.user_id
GROUP BY s.user_id;
    
