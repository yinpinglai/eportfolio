USE college;
ALTER TABLE students
ADD classroom_id INT(3) UNSIGNED,
FOREIGN KEY classroom_id REFERENCES classrooms(id);
