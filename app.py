from flask import Flask, jsonify, request
# from flask_cors import CORS  # Import CORS
from queries import TOP_CUSTOMERS_QUERY
from queries import GET_CUSTOMERS_QUERY
from queries import ADD_CUSTOMER_QUERY
from queries import DELETE_CUSTOMER_QUERY
from queries import GET_TRANSACTIONS_QUERY
from queries import ADD_TRANSACTION_QUERY
from queries import DELETE_TRANSACTION_QUERY
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
    
# // get cuomsters

@app.route('/customers', methods=['GET'])
def get_customers():
    # Alternate function logic
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(GET_CUSTOMERS_QUERY)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [{"customer_id": row[0], "name": row[1], "age": row[2], "created_at": row[3]} for row in results]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

    #///////Post method for customers
    
@app.route('/customers', methods=['POST'])
def add_customer():
    data = request.get_json()  # Parses JSON from the request body
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        params = (data['customer_id'], data['name'], data['age'], data['location'])
        cursor.execute(ADD_CUSTOMER_QUERY, params)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Customer added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    

                                                                    
                                                                    
  # // delete cuomster
@app.route('/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(DELETE_CUSTOMER_QUERY, (customer_id,))  # Pass the parameter as a tuple
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": f"Customer with ID {customer_id} deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500




# // get transtions 

@app.route('/transactions', methods=['GET'])
def get_transactions():
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(GET_TRANSACTIONS_QUERY)
        results = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [
            {
                "amount": float(row[0]) if row[0] is not None else None,  # Matches amount
                "product_id": row[1],  # Matches product_id
                "transaction_id": row[2],  # Matches transaction_id
                "purchase_date": row[3].strftime("%a, %d %b %Y %H:%M:%S GMT") if row[3] else None,  # Format purchase_date
                "customer_id": row[4],  # Matches customer_id
            }
            for row in results
        ]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

    ###/// post transactions

@app.route('/transactions', methods=['POST'])
def add_transaction():
    data = request.get_json()
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        params = (
            data['transaction_id'],
            data['customer_id'],
            data['product_id'],
            data['amount'],
            data['purchase_date'],
        )
        cursor.execute(ADD_TRANSACTION_QUERY, params)
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Transaction added successfully"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


#/// delete transactions
@app.route('/transactions/<int:transaction_id>', methods=['DELETE'])
def delete_transaction(transaction_id):
    conn = connect_to_redshift()
    if not conn:
        return jsonify({"error": "Unable to connect to Redshift"}), 500
    try:
        cursor = conn.cursor()
        cursor.execute(DELETE_TRANSACTION_QUERY, (transaction_id,))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"message": "Transaction deleted successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# // delete cuomster

# // add cusomter 

# // add transtions 

# you haave customer tables, transtions,

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9091, debug=True)
# from flask import Flask, jsonify
# from flask_cors import CORS  # Import CORS

# app = Flask(__name__)
# CORS(app)  # Enable CORS for the entire application

# @app.route('/top_customers', methods=['GET'])
# def get_top_customers():
#     # Your existing logic for fetching top customers
#     return jsonify([{"customer_id": 101, "total_spent": 500}])
