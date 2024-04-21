from dataclasses import dataclass
from abc import ABC, abstractmethod

@dataclass 
class Action(ABC):
    @abstractmethod
    def do(self, activator, target) -> bool:
        return False
    

    