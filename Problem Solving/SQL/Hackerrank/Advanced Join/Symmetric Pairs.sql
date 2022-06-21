-- https://www.hackerrank.com/challenges/symmetric-pairs/problem

SELECT a.x, a.y
FROM FUNCTIONS a 
JOIN FUNCTIONS b ON a.x = b.y AND a.y = b.x
GROUP BY a.x, a.y
HAVING COUNT(*) > 1 OR a.x < a.y
ORDER BY a.x