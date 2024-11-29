import boto3
import pandas as pd

# Define your S3 bucket and file names
bucket_name = "sales-data-bucket-123"
customers_file = "data/customers/customers.csv"
transactions_file = "data/transactions/transactions.csv"

# Connect to S3
s3 = boto3.client('s3')

try:
    # Fetch files from S3
    customers_obj = s3.get_object(Bucket=bucket_name, Key=customers_file)
    transactions_obj = s3.get_object(Bucket=bucket_name, Key=transactions_file)

    # Load data into Pandas DataFrames
    customers = pd.read_csv(customers_obj['Body'])
    transactions = pd.read_csv(transactions_obj['Body'])

    # Print the first few rows for verification
    print("Customers Data:")
    print(customers.head())

    print("\nTransactions Data:")
    print(transactions.head())

except s3.exceptions.NoSuchKey as e:
    print(f"Error: File not found in S3 - {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
