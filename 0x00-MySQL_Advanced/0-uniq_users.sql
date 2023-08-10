-- 0-uniq_users.sql
-- Users table
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    PRIMARY KEY(id)
);
