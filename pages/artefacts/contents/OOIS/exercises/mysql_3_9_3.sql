USE EPDriver;
ALTER TABLE drivers
RENAME COLUMN name driver_name VARCHAR(125) NOT NULL;
ALTER TABLE drivers
ADD COLUMN driver_age TINYINT(2) NOT NULL;
