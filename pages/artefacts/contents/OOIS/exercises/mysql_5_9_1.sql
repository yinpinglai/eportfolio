USE college;
SELECT classrooms.course_id, courses.id FROM classrooms
LEFT OUTER JOIN courses
ON classrooms.course_id = courses.id;
