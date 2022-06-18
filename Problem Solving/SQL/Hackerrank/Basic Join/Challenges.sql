-- https://www.hackerrank.com/challenges/challenges/problem?isFullScreen=true

SELECT h.hacker_id, h.name, COUNT(*) AS cnt
FROM Hackers h
JOIN Challenges c ON h.hacker_id = c.hacker_id
GROUP BY h.hacker_id, h.name
HAVING cnt = (
    SELECT COUNT(*)
    FROM Challenges
    GROUP BY hacker_id
    ORDER BY COUNT(*) DESC
    LIMIT 1
    )
OR
cnt in (
    SELECT cnt
    FROM (
        SELECT COUNT(*) as cnt
        FROM Challenges
        GROUP BY hacker_id
    ) AS sub_c
    GROUP BY cnt
    HAVING COUNT(cnt) = 1
)
ORDER BY cnt DESC, h.hacker_id;