-- 4-store.sql
-- SQL Trigger that decreases the amount of items on every purchase
DELIMITER $$
CREATE TRIGGER buy
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    UPDATE items
    SET quantity=(quantity - NEW.number)
    WHERE name=NEW.item_name;
END$$

DELIMITER ;
