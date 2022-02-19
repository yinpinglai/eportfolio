USE college;
SELECT * FROM classrooms
RIGHT OUTER JOIN courses
ON classrooms.course_id = courses.id;
