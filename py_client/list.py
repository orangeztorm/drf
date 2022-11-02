import requests
from getpass import getpass

# endpoint = "https://httpbin.org/status/200/"

# endpoint = "https://httpbin.org/anything"


auth_endpoint = "http://localhost:8000/api/auth/"

password = getpass()

auth_response = requests.post(auth_endpoint, json={'username': 'mac', 'password': password})  # Htt request

# print(get_response.text) # printts the data
print(auth_response.json()) 

endpoint = "http://localhost:8000/api/products/"


get_response = requests.get(endpoint,)  # Htt request

# print(get_response.text) # printts the data
print(get_response.json())  # printts the data in json
# print(get_response.status_code) # printts the status code
