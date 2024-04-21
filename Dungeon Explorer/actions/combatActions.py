from actions.baseActions import Action
from inputs.playerInput import listChoiceInput, pausePlayer
from entities.entity import Entity
from actions.baseActions import Action
from systems.entitySystems import PrintStats, calculateDefense

class AttackAction(Action):
    def do(self, activator, target) -> bool:
        if isinstance(target,Entity):
            print(f"{activator.name} Attacks!")
            pausePlayer()
            for equipmentSlot in activator.equipmentSlots:
                if equipmentSlot.equipment != None:
                    for attack in equipmentSlot.equipment.attackComponents:
                        damage = attack.calculateDamage()
                        damage = max(0,damage-calculateDefense(target))
                        print(f"{target.name} Takes {damage} {attack.atype.name} Damage!")
                        target.health.takeDamage(damage)
                        pausePlayer()
            return True
        else:
            return False

class LookAction(Action):
    def do(self, activator, target) -> bool:
        if isinstance(target,Entity):
            PrintStats(target)
        pausePlayer()
        return False

class PassAction(Action):
    def do(self, activator, target) -> bool:
        print(f"{activator.name} Passes")
        return True

class CheckSelfAction(Action):
    def do(self, activator, target) -> bool:
        PrintStats(activator)
        pausePlayer()
        return False

# Handle playe input in combat
class PlayerCombatChoice(Action):
    _actionsList = ['Attack','Look','Pass','Check Self']
    def do(self, activator, target) -> bool:
        choice = listChoiceInput("What would you like to do?",self._actionsList)
        if choice == 'Attack':
            action = AttackAction()
        if choice == 'Look':
            action = LookAction()
        if choice == 'Pass':
            action = PassAction()
        if choice == 'Check Self':
            action = CheckSelfAction()
        
        return action.do(activator=activator,target=target)

