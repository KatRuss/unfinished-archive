from dataclasses import dataclass, field
from components.baseComponents import StatsComponent, HealthComponent, WeightComponent, DescriptionComponent, CombatComponent
from components.inventoryComponents import EquipmentSlotComponent, InventoryComponent
from typing import List


@dataclass
class Entity:
    name: str = "Unamed Entity"
    location: object = None
    health: HealthComponent = None
    weight: WeightComponent = None
    equipmentSlots: List[EquipmentSlotComponent] = field(default_factory=list)
    inventory: InventoryComponent = None
    stats: StatsComponent = None
    tag: object = None
    descriptionComp: DescriptionComponent = None
    combat : CombatComponent = None
