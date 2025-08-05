import time

def temperatureConversion():
    while True:
        inputTemperatureType = input("Choose input temperature type [C,F,K] ->")
        
        match inputTemperatureType.upper():
            case "C":
                break
            case "F":
                break
            case "K":
                break
            case _:
                print("\nChoose the valid option\n")
                time.sleep(1)
                
    while True:
        outputTemperatureType = input("Choose Output temperature type [C,F,K] ->")
        
        if(inputTemperatureType == outputTemperatureType):
            print("\nYou can not convert from the same type\n")
            time.sleep(1)
            continue

        match outputTemperatureType.upper():
            case "C":
                break
            case "F":
                break
            case "K":
                break
            case _:
                print("\nChoose the valid option\n")
                time.sleep(1)


    while True:
        try:
           temperature = float(input("Please enter a temperature: "))
           break
        except ValueError:
            print("\nOops! That is not a valid number. Try again...")
                
    if(inputTemperatureType == "C" and outputTemperatureType == "F"):
        print(((9/5)*temperature)+32)
    elif(inputTemperatureType == "C" and outputTemperatureType == "K"):
        print(temperature+273.15)
    elif(inputTemperatureType == "K" and outputTemperatureType == "C"):
        print(temperature-273.15)
    elif(inputTemperatureType == "K" and outputTemperatureType == "F"):
        print(((temperature-273.15)*(9/5))+32)
    elif(inputTemperatureType == "F" and outputTemperatureType == "C"):
        print((temperature-32)*(9/5))
    else:
        print(((temperature-32)*(5/9))+273.15)


while True:
    primaryChoice = input("Choose a number on a keyboard coresponding to the number of the function:\n 1. Temperature Conversion\n 0. Exit\n Choose option->")

    match primaryChoice:
        case "1":
            temperatureConversion()
            break
        case "0":
            break
        case _:
            print("\nChoose the valid option\n")
            time.sleep(1)