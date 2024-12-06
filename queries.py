# queries.py
TOP_CUSTOMERS_QUERY = """
SELECT customer_id, SUM(amount) AS total_spent
FROM transactions
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
"""

# queries.py

# Customers Queries
GET_CUSTOMERS_QUERY = "SELECT * FROM customers;"
ADD_CUSTOMER_QUERY = "INSERT INTO customers (customer_id, name, age, location) VALUES (%s, %s, %s, %s);"
DELETE_CUSTOMER_QUERY = "DELETE FROM customers WHERE customer_id = %s;"

# Transactions Queries
GET_TRANSACTIONS_QUERY = "SELECT amount, product_id, transaction_id, purchase_date, customer_id FROM transactions;"
ADD_TRANSACTION_QUERY = "INSERT INTO transactions (transaction_id, customer_id, product_id, amount, purchase_date) VALUES (%s, %s, %s, %s, %s);"
DELETE_TRANSACTION_QUERY = "DELETE FROM transactions WHERE transaction_id = %s;"

# Products Queries
GET_PRODUCTS_QUERY = "SELECT * FROM products;"
ADD_PRODUCT_QUERY = "INSERT INTO products (product_id, name, price) VALUES (%s, %s, %s);"
DELETE_PRODUCT_QUERY = "DELETE FROM products WHERE product_id = %s;"



