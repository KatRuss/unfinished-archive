from entities.entity import Entity
from components.baseComponents import HealthComponent,StatsComponent,CombatComponent,DescriptionComponent
from components.inventoryComponents import EquipmentSlotComponent, itemSlotType
from components.tagsComponents import EnemyComponent
import data.weapons
from actions.combatActions import PassAction,AttackAction

Goblin = Entity(
    name= "Goblin",
    health=HealthComponent(12),
    stats=StatsComponent(dex=2),
    combat=CombatComponent(
        combatActions=[AttackAction(), PassAction()]),
    equipmentSlots=[EquipmentSlotComponent(itemSlotType.WEAPON,data.weapons.Mace)],
    tag=EnemyComponent(),
    descriptionComp=DescriptionComponent("Just a nastly little test goblin")
)

