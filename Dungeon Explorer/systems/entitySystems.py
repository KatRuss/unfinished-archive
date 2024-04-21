from formatting.textFormat import printTitle,printSubTitle,printListEntry
from entities.entity import Entity

def PrintStats(entity: Entity):
    #TODO: Make a generic PrintStats entity function
    printTitle(entity.name)
        
    if entity.health != None:
        printSubTitle("Health")
        printListEntry(f"HP: {entity.health.value}/{entity.health.maxHP}")
        printListEntry(f"{entity.name} is {'Dead' if entity.health.isDead else 'not Dead'}")
        
    if entity.weight != None:
        entity("Weight")
        entity(f"Weight: {entity.weight.weight}")
            
    if entity.equipmentSlots != []:
        printSubTitle("Equipent")
        print(f"{entity.name} appears to be equiped with: ")
        for equipentSlot in entity.equipmentSlots:
            if equipentSlot.equipment != None:
                printListEntry(equipentSlot.equipment)
        
    if entity.descriptionComp != None:
        printSubTitle("Description")
        print(entity.descriptionComp.value)

def calculateDefense(entity: Entity):
    result = 0
    for item in entity.equipmentSlots:
        if item.equipment != None and item.equipment.defenseComponents != []:
            for defense in item.equipment.defenseComponents:
                result += defense.amount
    return result