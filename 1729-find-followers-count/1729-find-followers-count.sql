# Write your MySQL query statement below
/*
steps:
    for each user_id, count total followers
    order by user_id ASC
*/
SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id ASC;