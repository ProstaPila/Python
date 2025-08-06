import time

#function that handles user input
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
    print(temperatureConversionLogic(inputTemperatureType,outputTemperatureType,temperature))

#function that does all the math :)
def temperatureConversionLogic(inputTemperatureType, outputTemperatureType, temperature):
    if(inputTemperatureType == "C" and outputTemperatureType == "F"):
        return(((9/5)*temperature)+32)
    elif(inputTemperatureType == "C" and outputTemperatureType == "K"):
        return(temperature+273.15)
    elif(inputTemperatureType == "K" and outputTemperatureType == "C"):
        return(temperature-273.15)
    elif(inputTemperatureType == "K" and outputTemperatureType == "F"):
        return(((temperature-273.15)*(9/5))+32)
    elif(inputTemperatureType == "F" and outputTemperatureType == "C"):
        return((temperature-32)*(9/5))
    else:
        return(((temperature-32)*(5/9))+273.15)

#menu of avaiable options
def converterMenu():
    primaryChoice = input("Choose a number on a keyboard coresponding to the number of the function:\n 1. Temperature Conversion\n 2. Metric and Imperial units converter \n 0. Exit\n Choose option->")

    match primaryChoice:
        case "1":
            temperatureConversion()  
        case "0":
            return 1
        case _:
            print("\nChoose the valid option\n")
            time.sleep(1)
            converterMenu()

#main loop
while True:
    workDecision="Y"

    match workDecision.upper():
        case "Y":
            if(converterMenu()==1):
                break
        case "N":
            break
        case _:
            print("\nChoose the valid option\n")
            time.sleep(1)
    
    workDecision = input("Do you want to make another operation [Y/N]? ")