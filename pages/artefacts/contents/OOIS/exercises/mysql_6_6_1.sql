SELECT
  min(stock) as least_stock,
  max(created_at) as newest_product,
  max(price) as product_max_price
FROM e_store.products;
