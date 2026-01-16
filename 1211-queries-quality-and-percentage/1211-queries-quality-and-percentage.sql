# Write your MySQL query statement below
/*
Queries
    query_name | result | position | rating

position: 1<=value<=500
rating: 1<=value<=5
query: poor if rating < 3

quality: avg(rating/position)
poor query percentage: (poor query * 100 / all queries)

Goal:
    query_name, quality, poor_query_percentage
    round 2 both quality and poor query_percentage

steps:
    group by query_name
    avg(rating/position)
    case statement to find poor queries , sum them and find avg
    round

*/

SELECT 
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(
        100 * SUM(
            CASE
                WHEN rating < 3 THEN 1
                ELSE 0
            END
        ) / COUNT(*),
    2) AS poor_query_percentage

FROM Queries
GROUP BY query_name