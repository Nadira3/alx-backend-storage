-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the weighted average score for a student
-- Note: An average score can be a decimal

-- Set the delimiter to avoid conflicts with the default semicolon terminator
DELIMITER //

-- Drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;

-- Create the procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(IN user_id INT)
BEGIN
    DECLARE avg_score DECIMAL;  -- Declare variable to store the average score

    -- Compute the average weighted score from the corrections table
    SELECT SUM(score * weight) / SUM(weight) INTO avg_score  -- Store the result in avg_score variable
    FROM corrections
    JOIN projects ON corrections.project_id = projects.id  -- Join corrections with projects to access weights
    WHERE corrections.user_id = user_id;

    -- Update the user's average score in the users table
    UPDATE users
    SET average_score = avg_score
    WHERE id = user_id;                                                                           
END;
//

-- Reset the delimiter back to the default                                                       
DELIMITER ;
