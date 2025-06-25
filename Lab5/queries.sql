USE my_guitar_shop;

-- 1) Show all products
SELECT * FROM products;

-- 2) Show all categories
SELECT * FROM categories;

-- 3) Show all addresses where state is 'CA'
SELECT * FROM addresses WHERE state = 'CA';

-- 4) Show products with list price greater than $500
SELECT product_name, list_price FROM products WHERE list_price > 500;

-- 5) Show all administrator email addresses
SELECT email_address FROM administrators;

-- 6) Show each product with its category name
SELECT 
    products.product_name, 
    categories.category_name
FROM 
    products
INNER JOIN 
    categories ON products.category_id = categories.category_id;

-- 7) Show orders with customer first and last names
SELECT 
    orders.order_id, 
    orders.order_date, 
    customers.first_name, 
    customers.last_name
FROM 
    orders
INNER JOIN 
    customers ON orders.customer_id = customers.customer_id;

-- 8) Show order items with product name and quantity
SELECT 
    order_items.order_id, 
    products.product_name, 
    order_items.quantity
FROM 
    order_items
INNER JOIN 
    products ON order_items.product_id = products.product_id;

-- 9) Show orders with shipping address details
SELECT 
    orders.order_id, 
    addresses.line1, 
    addresses.city, 
    addresses.state
FROM 
    orders
INNER JOIN 
    addresses ON orders.ship_address_id = addresses.address_id;

-- 10) Show each customer's orders and total quantity of items per order
SELECT 
    customers.first_name, 
    customers.last_name, 
    orders.order_id, 
    SUM(order_items.quantity) AS total_items
FROM 
    customers
INNER JOIN 
    orders ON customers.customer_id = orders.customer_id
INNER JOIN 
    order_items ON orders.order_id = order_items.order_id
GROUP BY 
    orders.order_id, customers.first_name, customers.last_name;

-- 11) Show count of addresses per state
SELECT 
    state, 
    COUNT(*) AS num_addresses
FROM 
    addresses
GROUP BY 
    state;

-- 12) Show average product price per category
SELECT 
    categories.category_name, 
    AVG(products.list_price) AS avg_price
FROM 
    products
INNER JOIN 
    categories ON products.category_id = categories.category_id
GROUP BY 
    categories.category_name;

-- 13) Show total number of orders per customer
SELECT 
    customers.first_name, 
    customers.last_name, 
    COUNT(orders.order_id) AS num_orders
FROM 
    customers
INNER JOIN 
    orders ON customers.customer_id = orders.customer_id
GROUP BY 
    customers.customer_id;

-- 14) Show total revenue (sum of item price minus discount) for all order items
SELECT 
    SUM(item_price - discount_amount) AS total_revenue
FROM 
    order_items;

-- 15) Show each order ID with customer's full name and total shipping plus tax amount
SELECT 
    orders.order_id, 
    customers.first_name, 
    customers.last_name, 
    (orders.ship_amount + orders.tax_amount) AS total_shipping_tax
FROM 
    orders
INNER JOIN 
    customers ON orders.customer_id = customers.customer_id;