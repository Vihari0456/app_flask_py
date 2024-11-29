from flask import Flask, jsonify
# from flask_cors import CORS  # Import CORS
from queries import TOP_CUSTOMERS_QUERY
from config import DATABASE
import psycopg2

app = Flask(__name__)

# CORS(app)  # Enable CORS for the entire application


def connect_to_redshift():
    try:
        conn = psycopg2.connect(
            host=DATABASE['host'],
            port=DATABASE['port'],
            user=DATABASE['user'],
            password=DATABASE['password'],
            dbname=DATABASE['dbname'],
            sslmode='require'
        )

        return conn
    except Exception as e:
        print(f"Error connecting to Redshift: {e}")
        return None

@app.route('/top_customers', methods=['GET'])
def get_top_customers():
    # Alternate function logic
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(TOP_CUSTOMERS_QUERY)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [{"customer_id": row[0], "total_spent": row[1]} for row in results]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
# from flask import Flask, jsonify
# from flask_cors import CORS  # Import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for the entire application

# @app.route('/top_customers', methods=['GET'])
# def get_top_customers():
#     # Your existing logic for fetching top customers
#     return jsonify([{"customer_id": 101, "total_spent": 500}])
