USE college;
SELECT * FROM classrooms
LEFT OUTER JOIN courses
ON classrooms.course_id = courses.id;
