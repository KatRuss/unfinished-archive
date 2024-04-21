from entities.item import Item
from components.baseComponents import WeightComponent, DescriptionComponent
from components.itemComponents import AttackComponent, DefenseComponent,dieType

Longsword = Item(
    name="Longsword",
    weight=WeightComponent(3.5),
    attackComponents=[AttackComponent(dice=dieType(6))],
    descriptionComp=DescriptionComponent("A common sword, used by savours and villains alike.\nWith skilled hands, a fine blade is all you will ever need.")
)

Mace = Item(
    name="Mace",
    weight=WeightComponent(3.5),
    attackComponents=[AttackComponent(flatDamage=2)],
    descriptionComp=DescriptionComponent("[Mace Description]")
)

Shield = Item(
    name="Shield",
    weight=WeightComponent(2.5),
    attackComponents=[AttackComponent(
                            dice=dieType(3),
                            flatDamage=1
                            )],
    defenseComponents=[DefenseComponent(amount=3)],
    descriptionComp="A half-busted and worn shield of iron and wood."
)

testWeaponList = [Longsword,Mace,Shield]