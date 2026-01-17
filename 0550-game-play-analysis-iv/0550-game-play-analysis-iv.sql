# Write your MySQL query statement below
/*
lag over event date and partition by player_id
filter ones with diff in days = 1

filter rows of first date for each player
join them with same table on date = date+ 1 and player id = player id

*/
WITH first_cte AS
(
    SELECT
        player_id,
        MIN(event_date) AS first_date
    FROM Activity
    GROUP BY player_id
)

SELECT 
    ROUND(
        COUNT(a.player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity),
        2
    )AS fraction
FROM Activity AS a
INNER Join first_cte AS f
ON 
    a.player_id = f.player_id AND 
    a.event_date = DATE_ADD(f.first_date, INTERVAL 1 DAY)
ORDER BY a.player_id



