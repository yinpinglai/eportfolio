USE e_store;
SELECT products.id, products.name, AVG(reviews.stars) as avg_stars
FROM products
JOIN reviews
ON products.id = reviews.product_id
GROUP BY products.name HAVING avg_stars BETWEEN 2 AND 3
ORDER BY products.id;
