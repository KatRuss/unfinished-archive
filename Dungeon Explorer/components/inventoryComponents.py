# FOR INVENTORY, EQUIPMENT SLOT,
from dataclasses import dataclass, field
from components.componentEnum import itemSlotType

# Gives an entity the capacity to hold items.
@dataclass
class InventoryComponent:
    items: list = field(default_factory=list)
    weightCap: float = 100
    
    def __post_init__(self):
        self.weight = 0

    def calculateWeight(self):
        result = 0
        for item in self.items:
            if not item.weight == None:
                result += item.weight.weight
        return result

@dataclass
class EquipmentSlotComponent:
    validSlotType: itemSlotType = None
    equipment: object = None