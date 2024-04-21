from dataclasses import dataclass,field
from typing import List, TYPE_CHECKING
from screen_action import QuitAppAction, ScreenAction
from input import L_InputSystem
from formatting import L_Formatter

@dataclass
class Screen:
    """_summary_
    """
    
    title: str = "Untitled Screen"
    introMessage: str = "[Intro message]"
    exitFunction: ScreenAction = QuitAppAction()
    optionsList: List[ScreenAction] = field(default_factory=list)
    inputSystem: L_InputSystem = field(default_factory=L_InputSystem)
    formatter: L_Formatter = field(default_factory=L_Formatter)

    def __str__(self) -> str:
        return self.title
        
    def exitScreen(self):
        self.exitFunction()

    def getOption(self):
        # get list of options, then case switch depending on what you want to do
        fullList: List[ScreenAction] = self.optionsList.copy()
        fullList.append(self.exitFunction)
        
        choice: ScreenAction = self.inputSystem.listChoiceInput(question="What would you like to do?", answerList=fullList)
        
        if choice != None:
            return choice.do()
        else:
            pass # Error handle

    def Show(self):
        self.formatter.printTitle(self.title)
        shouldReturn = False
        while not shouldReturn:
            print(f"You are currently at: {self.title}")
            shouldReturn = self.getOption()
