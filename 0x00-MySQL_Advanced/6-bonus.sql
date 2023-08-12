-- 6-add_bonus.sql
-- SQL Procedure that inserts a new correction into the corrections table
DELIMITER $$
CREATE 
PROCEDURE `AddBonus`(IN user_id INT,
IN project_name VARCHAR(255),
IN score INT)
BEGIN
    DECLARE pid INT;
    SELECT id INTO pid
    FROM projects
    WHERE name = project_name;

    IF pid IS NULL
    THEN
        INSERT INTO projects(name) VALUE(project_name);
        SELECT id INTO pid FROM projects WHERE name=project_name;
    END IF;

    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, pid, score);
END$$

DELIMITER ;
