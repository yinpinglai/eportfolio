USE e_store;
SELECT
  products.id,
  AVG(reviews.stars) AS "AVG(stars)"
FROM products
JOIN reviews
ON products.id = reviews.product_id
WHERE products.id = 4;
