-- 7-average_score.sql
-- SQL Procedure computing and storing the average score for a student
DELIMITER $$
CREATE PROCEDURE `ComputeAverageScoreForUser` (IN user_id INT)
BEGIN
    DECLARE u_id INT;
    SELECT id INTO u_id FROM users WHERE id=user_id;
    IF u_id IS NOT NULL
    THEN
        UPDATE users
        SET users.average_score=(
            SELECT AVG(corrections.score)
            FROM corrections
            WHERE corrections.user_id=user_id
            )
        WHERE users.id=user_id;
    END IF;
END$$

DELIMITER ;