/*
content = alphanumeric | '!' | ' '

GOAL:
    tweet_id of invalid tweets
    invalid means content length > 15

*/
SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;
