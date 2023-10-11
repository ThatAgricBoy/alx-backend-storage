-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score FLOAT;
    DECLARE total_count INT;
    DECLARE average FLOAT;

    -- Calculate the total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the total count of corrections for the user
    SELECT COUNT(*) INTO total_count
    FROM corrections
    WHERE user_id = user_id;

    -- Calculate the average score
    IF total_count > 0 THEN
        SET average = total_score / total_count;
    ELSE
        SET average = 0;
    END IF;

    -- Update the user's average_score in the users table
    UPDATE users
    SET average_score = average
    WHERE id = user_id;
END $$

DELIMITER ;
