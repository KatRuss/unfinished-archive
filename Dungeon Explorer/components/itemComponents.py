#FOR ATTACK, DEFENSE, USE
from dataclasses import dataclass, field
from components.componentEnum import attackType, dieType

@dataclass
class AttackComponent:
    dice: dieType = field(default_factory=lambda: dieType(4))
    diceNum: int = 1
    atype : attackType = attackType.PHYSICAL
    flatDamage: int = 0
    
    def calculateDamage(self):
        result = 0
        for x in range(0,self.diceNum):
            print("Damage die rolled")
            result += self.dice.RollDie()
        return result + self.flatDamage
    
@dataclass
class UseComponent:
    pass

@dataclass
class DefenseComponent:
    defType: attackType = attackType.PHYSICAL
    amount: float = 0