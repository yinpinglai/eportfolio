USE e_store;
SELECT
  products.name,
  products.price,
  products.stock,
  AVG(reviews.stars) AS avg_stars
FROM products
JOIN reviews
ON products.id = reviews.product_id
GROUP BY products.name HAVING avg_stars > 3
ORDER BY products.id;
