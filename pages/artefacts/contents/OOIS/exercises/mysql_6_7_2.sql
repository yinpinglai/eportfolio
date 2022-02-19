USE e_store;
SELECT 
  products.id,
  products.name AS product_name,
  products.price,
  reviews.stars
FROM products 
JOIN reviews 
ON products.id = reviews.product_id
WHERE products.id BETWEEN 3 and 4
ORDER BY products.id;
