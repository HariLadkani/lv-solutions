# Write your MySQL query statement below
#not refered by: null
#return names only
SELECT name
FROM Customer
WHERE referee_id != 2 or referee_id IS NULL;
