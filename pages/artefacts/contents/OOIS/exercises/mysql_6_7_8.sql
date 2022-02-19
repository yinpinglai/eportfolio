USE e_store;
SELECT
  products.id,
  SUM(reviews.stars)/COUNT(reviews.stars) AS avg_rating
FROM products
JOIN reviews
ON products.id = reviews.product_id
WHERE products.id = 4;
