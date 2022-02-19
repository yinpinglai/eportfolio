USE college;
SELECT * FROM classrooms
INNER JOIN courses
ON classrooms.course_id = courses.id;
