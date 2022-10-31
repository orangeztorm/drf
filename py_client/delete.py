from ast import Delete
import requests

# endpoint = "https://httpbin.org/status/200/"

# endpoint = "https://httpbin.org/anything"

product_id = input('What is the product id you want to use?\n')

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} not a valid id')


if product_id:
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete"

    get_response = requests.delete(endpoint,)  # Htt request

# print(get_response.text) # printts the data
    print(get_response.status_code)  # printts the data in json
# print(get_response.status_code) # printts the status code
