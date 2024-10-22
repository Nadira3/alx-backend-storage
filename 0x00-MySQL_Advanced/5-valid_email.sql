-- Set a custom delimiter to avoid conflicts with the default statement terminator
DELIMITER //

-- Drop the trigger if it already exists
DROP TRIGGER IF EXISTS reset_valid_email;

//

-- Create the trigger
CREATE TRIGGER reset_valid_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    -- Check if the email has been changed
    IF OLD.email != NEW.email THEN
        -- Reset the valid_email attribute if the email has changed
        SET NEW.valid_email = 0;  -- or you could set it to another default value
    END IF;
END;
//

-- Reset the delimiter back to the default
DELIMITER ;
