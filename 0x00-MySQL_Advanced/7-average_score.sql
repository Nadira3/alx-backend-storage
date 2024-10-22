-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the average score for a student
-- Note: An average score can be a decimal

-- Set the delimiter to avoid conflicts with the default semicolon terminator
DELIMITER //

-- Drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

-- Create the procedure
CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL(5,2);  -- Declare variable to store the average score

    -- Compute the average score from the corrections table
    SELECT AVG(score) INTO avg_score
    FROM corrections
    WHERE corrections.user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;
END;
//

-- Reset the delimiter back to the default
DELIMITER ;
