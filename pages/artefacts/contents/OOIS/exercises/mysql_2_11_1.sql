USE famous_scientists;
CREATE TABLE scientists (
  id INT(1) NOT NULL auto_increment,
  name VARCHAR(255) NOT NULL,
  discovery TEXT NOT NULL,
  year_of_birth INT(4) NOT NULL,
  year_of_death INT(4) DEFAULT NULL,
  PRIMARY_KEY(id)
) AUTO_INCREMENT = 1;
