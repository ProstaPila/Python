from TemperatureConversion import *
import time

#menu of avaiable options
def converterMenu():
    primaryChoice = input("Choose a number on a keyboard coresponding to the number of the function:\n 1. Temperature Conversion\n 2. Currency calculator \n 0. Exit\n Choose option->")

    match primaryChoice:
        case "1":
            temperatureConversion()
        case "0":
            return 1
        case _:
            print("\nChoose the valid option\n")
            time.sleep(1)
            converterMenu()