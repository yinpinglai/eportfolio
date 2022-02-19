USE blog;
SELECT posts.user_id, posts.body, users.name FROM posts
RIGHT OUTER JOIN users
ON posts.user_id = users.id;
