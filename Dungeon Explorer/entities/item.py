from dataclasses import dataclass, field
from typing import List
from entities.entity import Entity
from components.itemComponents import AttackComponent, DefenseComponent, UseComponent
from formatting.textFormat import printTitle, printSubTitle, printLine, printListEntry

@dataclass
class Item(Entity):
    attackComponents: List[AttackComponent] = field(default_factory=list)
    defenseComponents: List[DefenseComponent] = field(default_factory=list)
    useComponent: UseComponent = None

    def __str__(self) -> str:
        return self.name

    def printStats(self):
        printTitle(self.name)
        num = 1
        if self.attackComponents != []:
            printSubTitle("Attacks")
            for attack in self.attackComponents:
                printListEntry(f"{attack.diceNum}d{attack.dice.sides}{f'+{attack.flatDamage} ' if attack.flatDamage > 0 else ' '}{attack.atype.name} Damage")
                num+=1
        num = 1
        if self.defenseComponents != []:
            printSubTitle("Defences")
            for defense in self.defenseComponents:
                printListEntry(f"{defense.amount} {defense.defType.name} defense")
                num += 1
        # Insert Use Components here
        printSubTitle("Description")
        print(self.descriptionComp)