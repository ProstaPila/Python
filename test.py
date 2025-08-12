import requests

baseUrl = "https://api.nbp.pl/api/exchangerates/rates/A/chf"

print(requests.get(baseUrl).json())

