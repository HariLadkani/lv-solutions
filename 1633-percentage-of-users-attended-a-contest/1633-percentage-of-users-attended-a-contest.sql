# Write your MySQL query statement below
/*
Users
    user_id(pk) | user_name

Register
    user_id | contest_id

Goal:
    percentage of users registered for each contest_id
    order by percentage desc, contest_id asc
    round by 2 decimal

Steps:
    group by contest_id and compute count on user_id
    computer percentage = total count for each contest / total users in users table * 100
    order by 
    round


*/

SELECT 
    contest_id,
    ROUND((COUNT(user_id) / (SELECT COUNT(*) FROM Users)  * 100), 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC;
