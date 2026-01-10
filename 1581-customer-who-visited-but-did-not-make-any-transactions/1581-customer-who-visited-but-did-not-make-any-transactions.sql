# Write your MySQL query statement below

#customer_id not found in transactions and number of such visits for each customer_id

#9, 23, 54
SELECT
    customer_id,
    COUNT(*) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE transaction_id IS NULL
GROUP BY customer_id;