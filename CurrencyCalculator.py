import requests
import json
import time

def currencyCalculator():
    url = "https://api.nbp.pl/api/exchangerates/tables/A/"
    data = requests.get(url).json()
    rates = data[0]['rates']
    n = len(rates)
    currencyCodeValidation = []

    while True:
        for i in range(n):
            print(rates[i]['code'] + " " + rates[i]['currency'])
            currencyCodeValidation.append(rates[i]['code'])

        currencyChoice = input("Choose which currency you want to calculate from (PLN) to :").upper()
        if currencyChoice in currencyCodeValidation:
            print("ALl good proceed to calulate")
            break
        else:
            print("\nChoose the valid currency code\n")
            time.sleep(1)


