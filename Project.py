import time

def temperatureConversion():
    while True:
        inputTemperature = input("Choose input temperature type [C,F,K] ->")
        
        match inputTemperature.upper():
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