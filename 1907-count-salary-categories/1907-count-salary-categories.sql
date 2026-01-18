# Write your MySQL query statement below
WITH default_cte AS
(
    SELECT
        'Low Salary' AS category
    UNION ALL
    SELECT
        'Average Salary'
    UNION ALL
    SELECT 
        'High Salary'
),
category_cte AS
(
    SELECT
        (CASE 
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income >= 20000 AND income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END) AS category
    FROM Accounts
)
SELECT 
    d.category,
    (CASE 
        WHEN c.accounts_count IS NULL THEN 0
        ELSE c.accounts_count
    END) AS accounts_count
FROM default_cte AS d
LEFT JOIN 
    (SELECT
        category,
        COUNT(*) AS accounts_count
    FROM category_cte
    GROUP BY category) AS c
ON c.category = d.category

