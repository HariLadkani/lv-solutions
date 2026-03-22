-- Write your PostgreSQL query statement below
/*
Visits
visit_id(pk) | customer_id

Transactions
transaction_id(pk) | visit_id(FK) | amount

return customer_id in visits table who visit id not found in transactions and count of visits
*/
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON t.visit_id = v.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id
