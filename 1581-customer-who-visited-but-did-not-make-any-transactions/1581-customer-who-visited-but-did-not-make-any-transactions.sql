/*
goa:
    customer_id in Visits that do not have visit_id in Transaction
    group on customer_id to compute counts

*/
SELECT
    v.customer_id,
    COUNT(*) AS count_no_trans
FROM Visits AS v
LEFT JOIN Transactions AS t
ON v.visit_id = t.visit_id
WHERE t.visit_id IS NULL
GROUP BY v.customer_id;