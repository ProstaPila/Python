from Project_Functions import *


#main loop
workDecision="Y"
while True:
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