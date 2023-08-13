-- 101-average_weighted_score.sql
-- SQL Procedure that computes and stores the average weighted score for all students
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers ()
BEGIN
    DECLARE total_weight INT;

    SELECT SUM(weight) INTO total_weight FROM projects;

    UPDATE users
    SET average_score=(
        SELECT (SUM(corrections.score * projects.weight) / total_weight)
        FROM corrections
        INNER JOIN projects
        ON projects.id=corrections.project_id
        WHERE users.id = corrections.user_id
    );
END$$

DELIMITER ;
