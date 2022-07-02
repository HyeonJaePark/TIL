-- https://www.hackerrank.com/challenges/occupations/problem

SELECT
    GROUP_CONCAT(IF(Occupation = 'Doctor', Name, NULL)) AS 'Doctor', 
    GROUP_CONCAT(IF(Occupation = 'Professor', Name, NULL)) AS 'Professor', 
    GROUP_CONCAT(IF(Occupation = 'Singer', Name, NULL)) AS 'Singer', 
    GROUP_CONCAT(IF(Occupation = 'Actor', Name, NULL)) AS 'Actor'
FROM
(
SELECT a.*,
        (CASE @job WHEN a.OCCUPATION THEN @rownum:=@rownum+1 ELSE @rownum:=1 END) rnum,
        (@job:=a.OCCUPATION) job
    FROM OCCUPATIONS a,(SELECT @job:='', @rownum:=0 FROM DUAL) b
    ORDER BY Occupation, Name
) c
GROUP BY c.rnum