from enum import Enum
from dataclasses import dataclass

# -- DEFAULT INPUT MARKER --
class JUST_DIRECTIONS(Enum):
    RIGHT = 0,
    LEFT = 1,
    CENTRE = 2,

# -- FORMATTER DATACLASS --
@dataclass
class L_Formatter:
    _defaultInputMarker: str = ": "
    _defaultJustDir: int = JUST_DIRECTIONS.RIGHT
    _defaultInputJust: int = 6

    defaultTitleWrapper: str = "==="
    defaultQuestionWrapper: str = ""
    defaultErrorWrapper: str = "!!!"

    # -- Setters --
    def setTitleWrapper(self,wrapper: str): self.defaultTitleWrapper = wrapper
    def setQuestionWrapper(self,wrapper: str): self.defaultQuestionWrapper = wrapper
    def setErrorWrapper(self,wrapper: str): self.defaultErrorWrapper = wrapper
    
    def setDefaultInputMarker(self,newMarker: str) -> None: self._defaultInputMarker = newMarker
    def setDefaultInputJust(self,newJust: int) -> None: self._defaultInputJust = newJust
    
    def setDefaultJustDir(self,newDir) -> None: 
        if newDir in JUST_DIRECTIONS:
            self._defaultJustDir = newDir
        else:
            raise ValueError("Please only use a value within JUST_DIRECTIONS enum for 'setDefaultJustDir' method.")

    # -- Getters --
    def getDefaultInputMarker(self) -> str: return self.justify(self._defaultInputMarker)

    # -- Formatters --
    def justify(self,inp: str, just: int = _defaultInputJust, justDir = _defaultJustDir) -> str:
        """
        Helper function to justify a string. Mainly just to allow for consistant default values and less repetative code.
        """
        match justDir:
            case JUST_DIRECTIONS.RIGHT:
                return inp.rjust(just)
            case JUST_DIRECTIONS.LEFT:
                return inp.ljust(just)
            case JUST_DIRECTIONS.CENTRE:
                return inp.center(just)
            case _:
                raise ValueError(f"'{justDir}' is a not a valid input for 'justDir' in 'justify' function")

    # -- Headers --
    def printTitle(self,item: str): print(f"{self.defaultTitleWrapper}{item}{self.defaultTitleWrapper}")

    def printQuestion(self,item: str): print(f"{self.defaultQuestionWrapper}{item}{self.defaultQuestionWrapper}")
        
    def printError(self,item:str,fatal:bool = False):
        print(f"{self.defaultErrorWrapper}{item}{self.defaultErrorWrapper}")
        if fatal:
            exit()
        else:
            return False
