USE blog;
CREATE TABLE comments (
  id INT(3) UNSIGNED NOt NULL DEFAULT NULL auto_increment,
  body TEXT DEFAULT NULL,
  user_id INT(7) UNSIGNED NOT NULL DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (user_id) REFERENCES user(id)
) AUTO_INCREMENT = 1;
