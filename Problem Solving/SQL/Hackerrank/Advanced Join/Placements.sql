-- https://www.hackerrank.com/challenges/placements/problem

SELECT s.name
FROM friends f
JOIN packages p ON f.id = p.id
JOIN packages sp ON f.friend_id = sp.id
JOIN students s ON f.id = s.id
JOIN students ss ON sp.id = ss.id
WHERE p.salary < sp.salary
ORDER BY sp.salary