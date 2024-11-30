import psycopg2
import pandas as pd
import boto3

# Redshift database connection details
DATABASE = {
    'host': 'customer-analytics-cluster1.cote7e8kjcjg.us-east-1.redshift.amazonaws.com',
    'port': 5439,
    'user': 'admin',
    'password': 'Viharireddy0419',
    'dbname': 'dev'
}

# S3 bucket details
S3_BUCKET = "sales-data-bucket-123"
S3_CUSTOMERS_KEY = "data/customers/customers.csv"
S3_PRODUCTS_KEY = "data/products/products.csv"
S3_TRANSACTIONS_KEY = "data/transactions/transactions.csv"

def connect_to_redshift():
    """Connect to Redshift using psycopg2."""
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

def fetch_table_data(query):
    """Fetch data using psycopg2."""
    conn = connect_to_redshift()
    if not conn:
        return None
    try:
        # Execute query and fetch data
        cursor = conn.cursor()
        cursor.execute(query)
        columns = [desc[0] for desc in cursor.description]  # Column names
        data = cursor.fetchall()
        conn.close()
        # Convert to pandas DataFrame
        return pd.DataFrame(data, columns=columns)
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def save_to_csv(df, file_path):
    """Save the fetched data to a CSV file."""
    try:
        # Save DataFrame to CSV file
        df.to_csv(file_path, index=False)
        print(f"Data saved to {file_path}")
        return file_path
    except Exception as e:
        print(f"Error saving to CSV: {e}")
        return None

def upload_to_s3(file_path, bucket, s3_key):
    """Upload the CSV file to the S3 bucket."""
    s3 = boto3.client('s3')
    try:
        # Upload file to S3 bucket
        s3.upload_file(file_path, bucket, s3_key)
        print(f"Uploaded {file_path} to s3://{bucket}/{s3_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

def main():
    # Queries to fetch data from tables
    customers_query = "SELECT * FROM customers;"
    products_query = "SELECT * FROM products;"
    transactions_query = "SELECT * FROM transactions;"

    # Temporary file paths for storing CSVs
    customers_csv = "/tmp/customers.csv"
    products_csv = "/tmp/products.csv"
    transactions_csv = "/tmp/transactions.csv"

    # Fetch and process customers data
    customers_data = fetch_table_data(customers_query)
    if customers_data is not None:
        customers_file = save_to_csv(customers_data, customers_csv)
        if customers_file:
            upload_to_s3(customers_file, S3_BUCKET, S3_CUSTOMERS_KEY)

    # Fetch and process products data
    products_data = fetch_table_data(products_query)
    if products_data is not None:
        products_file = save_to_csv(products_data, products_csv)
        if products_file:
            upload_to_s3(products_file, S3_BUCKET, S3_PRODUCTS_KEY)

    # Fetch and process transactions data
    transactions_data = fetch_table_data(transactions_query)
    if transactions_data is not None:
        transactions_file = save_to_csv(transactions_data, transactions_csv)
        if transactions_file:
            upload_to_s3(transactions_file, S3_BUCKET, S3_TRANSACTIONS_KEY)

if __name__ == "__main__":
    main()
