-- Total revenue per product
SELECT
    product_name,
    SUM(quantity * price) AS total_revenue
FROM sales
GROUP BY product_name
ORDER BY total_revenue DESC;

-- Monthly revenue
SELECT
    DATE_TRUNC('month', order_date) AS month,
    SUM(quantity * price) AS monthly_revenue
FROM sales
GROUP BY month
ORDER BY month;
