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

#functions that does all the math :)
def fromCtoF (temperature):
    return(((9/5)*temperature)+32)

def fromCtoK (temperature):
    return(temperature+273.15)

def fromKtoC (temperature):
    return(temperature-273.15)

def fromKtoF (temperature):
    return(((temperature-273.15)*(9/5))+32)

def fromFtoC (temperature):
    return((temperature-32)*(5/9))

def fromFtoK (temperature):
    return(((temperature-32)*(5/9))+273.15)

conversionDict = {
    ("C","F"):fromCtoF,
    ("C","K"):fromCtoK,
    ("K","C"):fromKtoC,
    ("K","F"):fromKtoF,
    ("F","C"):fromFtoC,
    ("F","K"):fromFtoK,

}

def temperatureConversionLogic(inputTemperatureType, outputTemperatureType, temperature):
    func = conversionDict[(inputTemperatureType,outputTemperatureType)]
    return func(temperature)
    

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