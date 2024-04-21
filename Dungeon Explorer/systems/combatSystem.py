# For running the combat
from random import randint
from typing import List
from entities.entity import Entity
from formatting.textFormat import printTitle,printSubTitle
from components.tagsComponents import UserComponent

def getTurnOrder(entities: List[Entity]):
    for entity in entities:
        entity.combat.initiative = randint(1,20)+entity.stats.dex
    return sorted(entities,key=lambda entity: entity.combat.initiative, reverse=True)
    

def initCombat(player: Entity, enemy: Entity):
    combat = True
    turnOrder = getTurnOrder([player,enemy])
    
    player.combat.currentEnemy = enemy
    player.combat.parent = player
    enemy.combat.currentEnemy = player
    enemy.combat.parent = enemy
    
    printTitle("Combat!")
    printSubTitle(f"You have been attacked by {enemy.name}")
    while combat == True:
        for entity in turnOrder:
            if entity.health.isDead == True:
                print(f"{entity.name} is dead")
                entity.location = None
                if isinstance(entity.tag,UserComponent):
                    print("Game Over :(")
                    exit() #TODO: Have a real game-over function (restarting the game, going back to a main menu, etc.)
                combat = False
                break
            printSubTitle(f"{entity.name}'s Turn!")
            if entity.health.isDead == False:
                turnTaken = False
                while turnTaken == False:
                    turnTaken = entity.combat.doCombatAction()
            
    print("Combat is over!")