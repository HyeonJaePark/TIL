-- MySQL

SELECT HOUR(DATETIME), COUNT(1)
FROM ANIMAL_OUTS
WHERE 9 <= HOUR(DATETIME) AND HOUR(DATETIME) < 20
GROUP BY 1
ORDER BY 1;