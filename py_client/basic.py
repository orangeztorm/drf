import requests

# endpoint = "https://httpbin.org/status/200/"

endpoint = "https://httpbin.org/anything"

endpoint = "http://localhost:8000/"

get_response = requests.get(endpoint)  # Htt request

print(get_response.text) # printts the data