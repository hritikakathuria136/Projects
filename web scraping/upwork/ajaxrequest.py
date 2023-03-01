import requests
import json

# Set the API endpoint URL and the initial pagination token to None
url = 'https://www.amazon.com/hz/wishlist/slv/items'
pagination_token = None

# Define the data payload to send with the request
params = {
    'filter': 'unpurchased',
    'paginationToken': pagination_token,
    'itemsLayout': 'LIST',
    'sort': 'default',
    'type': 'wishlist',
    'lid': '2FQ6FORZLWS4K',
    'ajax': 'true'
}



while True:
    # Add the pagination token to the request params if it exists
    if pagination_token:
        params['paginationToken'] = pagination_token
    
    # Make the HTTP request
    response = requests.get(url, params=params)
    
    # Parse the JSON data
    response_json = json.loads(response.text)
    items = response_json.get('items')
    
    # Process the JSON data
    for item in items:
        product_name = item.get('product').get('productName')
        price = item.get('price').get('formattedAmount')
        
        # Do something with the product name and price, such as storing it in a database or writing it to a file
        print(product_name, price)
        
    # Check if there is more data to load
    if response_json.get('hasMoreResults'):
        pagination_token = response_json.get('paginationToken')
    else:
        break

# # Make the HTTP request to the API endpoint and retrieve the JSON data
# response = requests.get(api_url, params=data)
# response_json = response.json()

# # Extract the next pagination token from the JSON data
# pagination_token = response_json.get('paginationToken')

# # Process the JSON data
# # ...
# # Process the JSON data
# items = response_json.get('items')
# for item in items:
#     product_name = item.get('product').get('productName')
#     price = item.get('price').get('formattedAmount')
    
#     # Do something with the product name and price, such as storing it in a database or writing it to a file
#     print(product_name, price)


# # Make another HTTP request to the API endpoint with the new pagination token
# data['paginationToken'] = pagination_token
# response = requests.get(api_url, params=data)
# response_json = response.json()

# # Extract the next pagination token from the JSON data
# pagination_token = response_json.get('paginationToken')

# # Process the JSON data
# # ...

# # Repeat the process until there is no more data to load
