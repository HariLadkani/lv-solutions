# Write your MySQL query statement below
#content: alphanumerica, '!', ' '
#find ids where lenght of content > 15
SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;
