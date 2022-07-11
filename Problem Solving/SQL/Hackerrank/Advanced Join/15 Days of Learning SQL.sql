-- 

-- MYSQL if DENSE_RANK() support

SELECT 
    ooa.submission_date,
    ooa.cnt,
    oob.min_hacker_id, 
    oob.name
FROM (
    SELECT
        a.submission_date,
        COUNT(DISTINCT(hacker_id)) as cnt
    FROM (
        SELECT 
            DISTINCT(submission_date), 
            DENSE_RANK() OVER (ORDER BY submission_date) AS rank_date
        FROM submissions
    ) a
    JOIN (
        SELECT 
            submission_date, 
            hacker_id, 
            DENSE_RANK() OVER(PARTITION BY hacker_id ORDER BY submission_date) rank_hacker
        FROM submissions
    ) b ON  a.submission_date = b.submission_date AND
            a.rank_date = b.rank_hacker
    GROUP BY a.submission_date
) ooa
JOIN (
    SELECT
        oa.submission_date,
        oa.min_hacker_id,
        ob.name
    FROM (
        SELECT 
            c.submission_date,
            MIN(c.hacker_id) AS min_hacker_id
        FROM (
            SELECT
                submission_date,
                hacker_id, 
                COUNT(*) AS cnt
            FROM submissions
            GROUP BY submission_date, hacker_id
        ) c
        JOIN (
            SELECT
                d.submission_date,
                MAX(d.cnt) as max_cnt
            FROM (
                SELECT
                submission_date,
                hacker_id,
                COUNT(*) AS cnt
                FROM submissions
                GROUP BY submission_date, hacker_id
            ) d
            GROUP BY submission_date
        ) e ON  c.submission_date = e.submission_date AND
                c.cnt = e.max_cnt
        GROUP BY submission_date
    ) oa
    JOIN hackers ob ON oa.min_hacker_id = ob.hacker_id
    ORDER BY oa.submission_date
) oob ON ooa.submission_date = oob.submission_date
ORDER BY ooa.submission_date;

