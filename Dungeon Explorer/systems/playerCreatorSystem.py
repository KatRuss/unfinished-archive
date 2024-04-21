from typing import List
from actions.combatActions import PlayerCombatChoice

def ChooseItems():
    items = ()
    return items

def ChooseWeapon(weaponList):
    from inputs.playerInput import binaryChoiceInput, listChoiceInput,pausePlayer

    newWeapon = listChoiceInput("What weapon would you like?", weaponList)
    newWeapon.printStats()
    pausePlayer()
    if binaryChoiceInput("Would you like this weapon?"):
        return newWeapon
    else:
        print("My mistake...")
        return ChooseWeapon(weaponList)

def createEquipmentSlots():
    from components.inventoryComponents import EquipmentSlotComponent
    from data.weapons import testWeaponList
    from components.componentEnum import itemSlotType
    
    equipmentSlots:List[EquipmentSlotComponent] = list()
    
    equipmentSlots.append(EquipmentSlotComponent(itemSlotType.WEAPON,ChooseWeapon(testWeaponList)))
    equipmentSlots.append(EquipmentSlotComponent(itemSlotType.ARMOUR))
    
    return equipmentSlots

def createPlayerInventory():
    from components.inventoryComponents import InventoryComponent

    newInventory = InventoryComponent(
        items=ChooseItems(),
        weightCap=100
    )
    newInventory.weight = newInventory.calculateWeight()
    return newInventory

def createPlayerStats():
    from components.baseComponents import StatsComponent
    from inputs.playerInput import binaryChoiceInput
    
    stats = StatsComponent()
    stats.RollStats()
    print("Current your Stats are:")
    stats.PrintStats()

    if binaryChoiceInput(question= "Would you like to keep these stats?"):
        return stats
    else:
        print("Rerolling...")
        return createPlayerStats()

def createPlayerName():
    from inputs.playerInput import genericTextInput, binaryChoiceInput
    
    print("What is your name?")
    newName = genericTextInput()
    
    if binaryChoiceInput(question= f"Is {newName} your name?"):
        return newName
    else:
        print("My Mistake...")
        return createPlayerName()

def playerCreator():
    from entities.item import Entity
    from components.tagsComponents import UserComponent
    from components.baseComponents import CombatComponent,HealthComponent
    
    newPlayer = Entity()
    newPlayer.tag = UserComponent()
    newPlayer.combat = CombatComponent(
        combatActions=[
            PlayerCombatChoice()
        ]
    )
    print("=== CHARACTER CREATION ===")
    newPlayer.name = createPlayerName()
    print("--------- Stats ----------")
    newPlayer.stats = createPlayerStats()
    print("------- Inventory --------")
    newPlayer.inventory = createPlayerInventory()
    newPlayer.equipmentSlots = createEquipmentSlots()
    newPlayer.health = HealthComponent(10+newPlayer.stats.might)

    return newPlayer