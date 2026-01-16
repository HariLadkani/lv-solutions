# Write your MySQL query statement below
/*
Transactions
    id(pk) | country | state | amount | trans_date


goal:
    for each month and country:
        # of transactions
        total amount
        # of approved transactions
        #total amount of approved transactions

steps:
    partition by month, country
    sum(transactions)
    use case statements to filter approved or non approved
*/

SELECT 
    DATE_FORMAT(trans_date, '%Y-%m') AS month,
    country,
    COUNT(*) AS trans_count,
    SUM(
        CASE 
            WHEN state = 'approved' THEN 1
            ELSE 0
        END
    ) AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(
        CASE 
            WHEN state = 'approved' THEN amount
            ELSE 0
        END
    ) AS approved_total_amount
FROM Transactions
GROUP BY MONTH(trans_date), YEAR(trans_date), country
