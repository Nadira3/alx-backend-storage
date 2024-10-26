-- SQL script that creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0

-- set delimiter to avoid conflict in parsing statement
DELIMITER //

-- create function to handle logic
CREATE FUNCTION SafeDiv (
        IN a INT,
        IN b INT
) RETURNS INT
BEGIN
    -- Check if the second number is 0
    IF b = 0 THEN
        RETURN 0; -- Return 0 if b is 0
    ELSE
        RETURN a / b; -- Perform the division if b is not 0
    END IF;
END //

-- reset delimiter to ;
DELIMITER ;
