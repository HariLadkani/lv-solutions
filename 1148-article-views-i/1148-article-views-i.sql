# Write your MySQL query statement below
#duplicate rows possible  because no primary key

#find author_id where viewer_id =  authord_id
#order by id ASC
SELECT DISTINCT author_id AS id
FROM Views
WHERE viewer_id = author_id
ORDER BY author_id ASC;