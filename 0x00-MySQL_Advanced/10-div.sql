-- SQL script that creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0

-- Set delimiter to avoid conflict in parsing statement
DELIMITER //

-- Create function to handle logic
CREATE FUNCTION SafeDiv (
        IN a INT,
        IN b INT
) RETURNS DECIMAL(10, 4)  -- You can adjust the precision as needed
BEGIN
    -- Declare the variable first
    DECLARE result DECIMAL(10, 4);
    
    -- Check if the second number is 0
    IF b = 0 THEN
        RETURN 0; -- Return 0 if b is 0
    ELSE
        SET result = a / b; -- Perform the division

        -- Check if result is an integer
        IF result = FLOOR(result) THEN
            RETURN CAST(result AS UNSIGNED); -- Return as INT if it’s an integer
        ELSE
            RETURN result; -- Return the decimal result
        END IF;
    END IF;
END //

-- Reset delimiter to ;
DELIMITER ;
