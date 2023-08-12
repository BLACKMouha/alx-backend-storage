-- 11-need_meeting.sql
-- 
CREATE VIEW need_meeting AS
    SELECT * FROM students
    WHERE score < 80
    AND
    (last_meeting IS NULL OR (last_meeting - (INTERVAL 1 MONTH + CURDATE()) < 30 ));
