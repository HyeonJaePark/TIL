-- https://www.hackerrank.com/challenges/print-prime-numbers/problem

CREATE TABLE PrimeNumber(num INT PRIMARY KEY);

DELIMITER $$
CREATE PROCEDURE prime()
BEGIN
    DECLARE i INT;
    DECLARE j INT;
    DECLARE isPrime INT DEFAULT 0;
    SET i = 2;
    
    WHILE (i <= 1000) DO
        SET j = 2;
        SET isPrime = 0;
        WHILE (j < i) DO
            IF (i % j = 0) THEN
                SET isPrime = isPrime + 1;
            END IF;
            SET j = j + 1;
        END WHILE;
        IF (isPrime = 0) THEN
            INSERT INTO PrimeNumber VALUES (i);
        END IF;
        SET i = i + 1;
    END WHILE;
END$$
DELIMITER ;

CALL prime();

SELECT GROUP_CONCAT(num separator '&') FROM PrimeNumber;