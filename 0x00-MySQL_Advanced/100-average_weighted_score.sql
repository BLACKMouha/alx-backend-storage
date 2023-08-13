-- 100-average_weighted_score.sql
-- SQL Procedure that computes and stores the average weighted score for a student
DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser (IN user_id INT)
BEGIN
    DECLARE total_weight INT;
    DECLARE avg_weighted_score FLOAT;
    DECLARE u_id INT;

    SELECT id INTO u_id FROM users WHERE id=user_id;
    IF u_id IS NOT NULL
    THEN
        SELECT SUM(weight) INTO total_weight FROM projects;

        SELECT SUM(corrections.score * projects.weight)
        INTO avg_weighted_score
        FROM corrections
        LEFT JOIN projects
        ON projects.id = corrections.project_id
        WHERE corrections.user_id=u_id;

        UPDATE users
        SET users.average_score=(avg_weighted_score / total_weight)
        WHERE users.id=u_id;
    END IF;
END$$

DELIMITER ;
