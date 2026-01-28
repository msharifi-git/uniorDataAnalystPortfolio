-- Sample sales table
CREATE TABLE sales (
    order_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    quantity INT,
    price DECIMAL(10,2),
    order_date DATE
);

-- Insert some example data
INSERT INTO sales VALUES
(1, 'Laptop', 2, 1200.00, '2025-01-10'),
(2, 'Mouse', 5, 15.50, '2025-01-11'),
(3, 'Keyboard', 3, 25.00, '2025-02-05'),
(4, 'Monitor', 1, 200.00, '2025-02-07'),
(5, 'Laptop', 1, 1200.00, '2025-03-03');
