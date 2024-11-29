# # # import pandas as pd
# # import matplotlib.pyplot as plt
# # import requests

# # # Fetch data from the Flask endpoint
# # response = requests.get("http://127.0.0.1:5000/top_customers")

# # # Check for successful response
# # if response.status_code == 200:
# #     data = response.json()

# #     # Convert the data to a Pandas DataFrame
# #     df = pd.DataFrame(data)

# #     # Print the data for verification
# #     print("Fetched Data:")
# #     print(df)
# # else:
# #     print(f"Failed to fetch data. Status Code: {response.status_code}")

# import requests  # To fetch data from the Flask API
# import pandas as pd  # To structure the data
# import matplotlib.pyplot as plt  # To visualize the data

# # Step 1: Fetch data from the /top_customers API
# response = requests.get("http://127.0.0.1:5000/top_customers")  # Flask API endpoint

# # Step 2: Check if the API call was successful
# if response.status_code == 200:
#     # Step 3: Convert the JSON response into a DataFrame
#     data = response.json()
#     df = pd.DataFrame(data)

#     # Print the data for verification
#     print("Fetched Data:")
#     print(df)

#     # Step 4: Create a bar chart
#     plt.bar(df['customer_id'], df['total_spent'], color='skyblue')
#     plt.title('Top Customers by Spending')  # Add a title
#     plt.xlabel('Customer ID')  # Label for X-axis
#     plt.ylabel('Total Spent')  # Label for Y-axis
#     plt.xticks(df['customer_id'])  # Show customer IDs on the X-axis
#     plt.tight_layout()  # Adjust layout to fit titles and labels

#     # Step 5: Display the chart
#     plt.show()
# else:
#     print(f"Failed to fetch data. Status Code: {response.status_code}")


import requests
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Fetch data from the API
response = requests.get("http://127.0.0.1:5000/top_customers")  # Flask API endpoint

# Step 2: Check if the API call was successful
if response.status_code == 200:
    # Convert the JSON response into a DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Print the data for verification
    print("Fetched Data:")
    print(df)

    # Proceed to visualization
else:
    print(f"Failed to fetch data. Status Code: {response.status_code}")
