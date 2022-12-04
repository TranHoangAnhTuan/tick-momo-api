import requests
from pprint import pprint

endpoint = "http://127.0.0.1:8000/momo"
data = requests.get(endpoint)

pprint(data.text)