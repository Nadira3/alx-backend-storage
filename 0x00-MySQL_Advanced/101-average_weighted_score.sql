-- script that creates a stored procedure ComputeAverageScoreForUser
-- that computes and store the weighted average score for a student
-- Note: An average score can be a decimal

-- Set the delimiter to avoid conflicts with the default semicolon terminator
DELIMITER //

-- Drop procedure if it already exists
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

-- Create the procedure
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DECLARE done INT DEFAULT FALSE;
	DECLARE user_id INT;
    	DECLARE avg_score FLOAT;  -- Declare variable to store the average score

	-- declare cursor to iterate through all users
	DECLARE user_cursor CURSOR FOR
		SELECT id FROM users;
	
	-- declare a handler for when there are no more rows
	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

	-- open the cursor
	OPEN user_cursor;

	read_users: LOOP
		-- fetch the next user id into the variable user_id
		FETCH user_cursor INTO user_id;

		IF done THEN
			LEAVE read_users;
		END IF;

    		-- Compute the average weighted score from the corrections table
    		SELECT SUM(score * weight) / SUM(weight) INTO avg_score  -- Store the result in avg_score variable
    		FROM corrections
    		JOIN projects ON corrections.project_id = projects.id  -- Join corrections with projects to access weights
    		WHERE corrections.user_id = user_id;

    		-- Update the user's average score in the users table
    		UPDATE users
    		SET average_score = avg_score
    		WHERE id = user_id;

	END LOOP read_users;

	-- close the cursor
	CLOSE user_cursor;
END;
//

-- Reset the delimiter back to the default                                                       
DELIMITER ;
