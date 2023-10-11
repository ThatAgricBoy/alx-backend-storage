-- SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
DELIMITER //

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
BEGIN
    DECLARE total_score DECIMAL(10, 2);
    DECLARE total_projects INT;
    DECLARE average DECIMAL(10, 2);

    -- Compute total score for the user
    SELECT SUM(score) INTO total_score
    FROM corrections
    WHERE user_id = user_id;

    -- Compute total projects for the user
    SELECT COUNT(*) INTO total_projects
    FROM corrections
    WHERE user_id = user_id;

    -- Compute average score
    IF total_projects > 0 THEN
        SET average = total_score / total_projects;
        UPDATE users
        SET average_score = average
        WHERE id = user_id;
    ELSE
        SET average = 0;
    END IF;
END //

DELIMITER ;
