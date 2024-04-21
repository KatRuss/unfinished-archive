# For STATS, WEIGHT, HEALTH, DESCRIPTION
from dataclasses import dataclass, field
from random import randint
from typing import List
from actions.baseActions import Action

# Gives an entity the capacity to have the in game stats. Used for players and enemies.
@dataclass
class StatsComponent:
    might: int = 0
    mind: int = 0
    dex: int = 0
    cha: int = 0

    def RollStats(self):
        self.might = randint(1,6) + randint(1,6)
        self.mind = randint(1,6) + randint(1,6)
        self.dex = randint(1,6) + randint(1,6)
        self.cha = randint(1,6) + randint(1,6)
    
    def PrintStats(self):
        print(f"Might: {self.might}")
        print(f"Mind: {self.mind}")
        print(f"Dexterity: {self.dex}")
        print(f"Charisma: {self.cha}")


@dataclass
class HealthComponent:
    maxHP: int = 1
    
    def __post_init__(self):
        self.isDead = False
        self.value = self.maxHP
        
    def takeDamage(self,damage: int):
        self.value -= damage
        if self.value <= 0:
            self.isDead = True

# Gives entity the capacity for weight. Used in regards to picking things up and
# Adding them into the player's inventory
@dataclass
class WeightComponent:
    weight: float = 0
    

@dataclass
class DescriptionComponent:
    value: str = "no description"
    
    def __str__(self) -> str:
        return self.value

# The entity has the capacity to initiate combat, have actions in combat, etc.
@dataclass
class CombatComponent:
    parent: object = None
    currentEnemy: object = None
    combatActions : List[Action] = field(default_factory=list)

    def doCombatAction(self, id: int = 0):
        return self.combatActions[id].do(activator=self.parent,target=self.currentEnemy)
    
    def __post_init__(self):
       self.initiative: int = 0 