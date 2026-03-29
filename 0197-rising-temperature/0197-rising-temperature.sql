-- Write your PostgreSQL query statement below
/*
order by recordDate

lag over temperature. if current temp > lag, return that as valid id
if lag returns none, ignore that id


*/
WITH cte AS (
SELECT
    id,
    LAG(temperature) OVER (ORDER BY recordDate) AS prev_temp,
    temperature,
    LAG(recordDate) OVER (ORDER BY recordDate) AS prior_date,
    recordDate
FROM Weather
)

SELECT id FROM cte WHERE temperature > prev_temp and (recordDate - prior_date) = 1
