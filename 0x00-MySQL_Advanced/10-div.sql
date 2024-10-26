-- SQL script that creates a function SafeDiv that divides (and returns) the first
-- by the second number or returns 0 if the second number is equal to 0

-- Set delimiter to avoid conflict in parsing statement
DELIMITER //
DROP FUNCTION IF EXISTS SafeDiv;
-- Create function to handle logic
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS DOUBLE
BEGIN
    IF b = 0 THEN
        RETURN 0; 
    ELSE
        RETURN CAST(a AS DECIMAL(20,15)) / CAST(b AS DECIMAL(20,15));
    END IF;
END
