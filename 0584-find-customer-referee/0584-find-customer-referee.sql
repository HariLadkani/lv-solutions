/*
output: return name where
id not equal to 2 or id is null
*/
SELECT name
FROM Customer
WHERE referee_id  != 2 OR referee_id  is NULL;