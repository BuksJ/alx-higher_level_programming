-- creates the table force_name on your MySQL server
-- Creates the table force_name.
CREATE TABLE IF NOT EXISTS force_name (
id INT NOT NULL AUTO_INCREMENT,
name VARCHAR(256) NOT NULL,
PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
