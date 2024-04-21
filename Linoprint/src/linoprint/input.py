"""
A list of modules regarding taking input in a standard, formatted way.
"""
import re
from dataclasses import dataclass, field
from formatting import L_Formatter 
from enum import Enum

class default_inputs(Enum):
    YES = 'y'
    NO  = 'n'

@dataclass
class L_InputSystem:
    """"""

    formatter: L_Formatter = field(default_factory=L_Formatter)

    # -- General inputs --
    def wait():
        """A generic command to pause the application and wait for the user to continue, mainly to make reading large amounts of text easier."""

        input("**Press Enter to Continue**")
        print("---------------------------")

    # -- Question inputs --
    def _printQuestionAndResonse(self,question: str = "", positive: str = None, negative: str = None):
        """internal function for printing the question and the user response in a standardised way."""
        if question != "": 
            self.formatter.printQuestion(f"{question} {f'({positive}/{negative})' if positive != None and negative != None else ''}")
        return input(self.formatter.getDefaultInputMarker())

    def lineInput(self,question: str = "", validation: str = ""):
        """Get a written input from the user that is returned as a string. Useful for things such as typing in passwords or creating names for new tasts, etc. """
        
        answer = self._printQuestionAndResonse(question)
        if answer.strip() != "":
            #Validation
            if validation != "":
                for char in answer:
                    if re.match(validation,char): 
                        # Validation catches illegal character
                        print(f"Response includes illegal character '{char}'")
                        return self.typedInput(question)
                return answer # nothing illegal was found
            else:
                return answer
        else:
            print("Please write a value.")
            return self.typedInput(question)   

    def multiLineInput(self, question: str = "", validation: str = ""):
        """ """
        shouldExit = False
        lines = []
        self.formatter.printQuestion(f"{question} (Type 'EXIT' to finish writing)")
        while not shouldExit:
            answer = self.lineInput(validation=validation) 
            if answer == "EXIT":
                shouldExit = True
            else:
                lines.append(answer)
        return lines

    def binaryChoiceInput(self,question: str = "", positive: str = default_inputs.YES.value, negative: str = default_inputs.NO.value):
        """get a yes/no choice input from the user."""

        answer = self._printQuestionAndResonse(question, positive, negative).strip()
        if answer == positive:
            return True
        elif answer == negative:
            return False
        else:
            print(f"{answer} is not a valid answer")
            return self.binaryChoiceInput(question,positive,negative)

    def listChoiceInput(self,question: str = "", answerList: list = []):
        """Lets user choose an option from a list of choices"""
        self.formatter.printQuestion(question)
        
        for x in range(len(answerList)):
            print(f"{x+1}. {answerList[x]}")
            
        choice = input(self.formatter.getDefaultInputMarker())
        
        if choice.isdigit() and int(choice) > 0 and int(choice) <= len(answerList):
            return answerList[int(choice)-1]
        else:
            print(f"{choice} is not a valid choice")
            return self.listChoiceInput(question,answerList)
