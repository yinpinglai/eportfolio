USE e_store;
SELECT sum(stock) as total_stock FROM products;
SELECT
  products.id, sum(reviews.stars) AS total_stars
FROM products
JOIN reviews
ON products.id = reviews.product_id
WHERE products.id = 4;
