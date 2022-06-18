-- https://www.hackerrank.com/challenges/harry-potter-and-wands/problem?isFullScreen=true

SELECT w.id, p.age, w.coins_needed, w.power
FROM Wands w
JOIN Wands_Property p ON w.code = p.code
WHERE p.is_evil = 0 
AND
w.coins_needed = (
    SELECT MIN(sub_w.coins_needed)
    FROM Wands sub_w
    JOIN Wands_Property sub_p ON sub_w.code = sub_p.code
    WHERE sub_p.is_evil = 0
    AND
    sub_w.power = w.power
    AND
    sub_p.age = p.age
)
ORDER BY w.power DESC, p.age DESC;