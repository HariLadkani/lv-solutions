/*
OUTPUT: name, population, area where 
    area > 3000000
        OR
    population > 25000000
*/
SELECT
    name, 
    population,
    area
FROM World
WHERE 
    area >= 3000000 OR
    population >= 25000000;