import requests

# endpoint = "https://httpbin.org/status/200/"

# endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    "title": "hello world my old friend",
    "price": 123.00
}

get_response = requests.put(endpoint,json=data)  # Htt request

# print(get_response.text) # printts the data
print(get_response.json())  # printts the data in json
# print(get_response.status_code) # printts the status code
