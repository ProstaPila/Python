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
            #print("ALl good proceed to calulate")
            break
        else:
            print("\nChoose the valid currency code\n")
            time.sleep(1)
    
    while True:
        try:
           inputValue = float(input("Please enter a value that you want to convert: "))
           break
        except ValueError:
            print("\nOops! That is not a valid number. Try again...") 

    getCurrencyData = f"https://api.nbp.pl/api/exchangerates/rates/A/{currencyChoice}"
    currencyData = requests.get(getCurrencyData).json()
    exchangeRate = currencyData['rates'][0]['mid']

    print("Your value is:", calculateCurrencyValue(inputValue, exchangeRate), currencyChoice)



def calculateCurrencyValue(value, exchangeRate):
    return round(value / exchangeRate,2)

