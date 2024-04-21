from enum import Enum
from formatting.textFormat import printThinLine

class genericKeyInputs(Enum):
    YES = "y"
    NO = "n" 

#This is to control the flow of information being given to the player, so the player has time to read everything that is being outputted to them
def pausePlayer():
    dummy = input(".. Press ENTER to continue ..")
    
def genericTextInput():
    printThinLine()
    text = input(">> ")
    return text
    
def binaryChoiceInput(question:str, aInput: str = genericKeyInputs.YES.value, bInput: str = genericKeyInputs.NO.value):
    printThinLine()
    print(question + f" ({aInput}/{bInput})")
    decision = input(">> ")
    printThinLine()
    if decision == aInput:
        return True
    elif decision == bInput:
        return False
    else:
        print(f"{decision} is not a valid key")
        print(f"The Valid Keys are [{aInput}/{bInput}]")
        return binaryChoiceInput(question,aInput,bInput)
    
def listChoiceInput(question:str, li:list):
        printThinLine()
        print(question)
        for x in range(0,len(li)):
             print(f"{x+1}: {li[x]}")
        choice = genericTextInput()
        printThinLine()
        if choice.isnumeric() and int(choice) >= 1 and int(choice) <= len(li):
            return li[int(choice)-1]
        else:
            print(f"{choice} is not a valid key")
            return listChoiceInput(question,li)
        
