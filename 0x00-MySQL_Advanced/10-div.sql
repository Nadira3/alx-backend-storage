-- SQL script that creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0

-- select database;
DROP FUNCTION IF EXISTS SafeDiv;

-- Set delimiter to avoid conflict in parsing statement
DELIMITER //

-- Create function to handle logic
CREATE FUNCTION SafeDiv (
    IN a INT,
    IN b INT
) RETURNS DECIMAL(10, 6)
BEGIN
    DECLARE result DECIMAL(10, 6);

    IF b = 0 THEN
        RETURN 0; -- Return 0 if b is 0
    ELSE
        SET result = a / b; -- Perform the division

        IF result = FLOOR(result) THEN
            RETURN CAST(result AS UNSIGNED); -- Return as INT
        ELSE
            RETURN result; -- Return as DECIMAL
        END IF;
    END IF;
END //

DELIMITER ;
