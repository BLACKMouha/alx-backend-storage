-- 11-need_meeting.sql
-- 
CREATE VIEW need_meeting AS
    SELECT name FROM students
    WHERE score < 80
    AND
    (last_meeting IS NULL
        OR
        DATEDIFF(last_meeting, CURDATE()) <= 30
    );
