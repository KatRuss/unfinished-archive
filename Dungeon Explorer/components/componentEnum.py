# For component enums (item slots, damage types, etc)
from enum import Enum
from dataclasses import dataclass
from random import randint

class attackType(Enum):
    PHYSICAL = 0
    ASTRIL = 1
    FIRE = 2
    LIGHTNING = 3

class itemSlotType(Enum):
    WEAPON = 1
    ARMOUR = 2
    
# Represents a kind of die. e.g. sides = 6 means a standard six-sided die.
@dataclass
class dieType():
    sides: int
    
    def RollDie(self):
        roll = randint(1,self.sides)
        print(f"Rolled: {roll}")
        return roll