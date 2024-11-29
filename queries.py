# queries.py
TOP_CUSTOMERS_QUERY = """
SELECT customer_id, SUM(amount) AS total_spent
FROM transactions
GROUP BY customer_id
ORDER BY total_spent DESC
LIMIT 10;
"""
