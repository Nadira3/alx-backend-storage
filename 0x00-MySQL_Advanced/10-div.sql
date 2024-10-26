-- SQL script that creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0

-- Set delimiter to avoid conflict in parsing statement
DELIMITER //

-- Create function to handle logic
CREATE FUNCTION SafeDiv (
    IN a INT,
    IN b INT
) RETURNS DOUBLE
BEGIN
    DECLARE result DOUBLE;

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
