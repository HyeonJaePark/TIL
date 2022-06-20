-- https://www.hackerrank.com/challenges/the-report/problem

SELECT IF(g.grade > 7, s.name, NULL), g.grade, s.marks
FROM Students s, Grades g
WHERE s.marks between min_mark and max_mark
ORDER BY g.grade DESC, s.name, s.marks ASC;