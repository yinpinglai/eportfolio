USE e_store;
SELECT COUNT(stock) AS total_product_count FROM products;
SELECT
  products.id,
  COUNT(reviews.stars) AS stars_fields_count
FROM products
JOIN reviews
ON products.id = reviews.product_id
WHERE products.id = 4;
