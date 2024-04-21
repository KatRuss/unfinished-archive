from systems.combatSystem import initCombat
from components.tagsComponents import UserComponent
from formatting.textFormat import printTitle, printSubTitle, printLine
from inputs.playerInput import pausePlayer
from actions.roomActions import PlayerRoomChoiceAction
from entities.room import Room
from components.roomsComponents import RoomConnectionComponent, LockComponent

def enterRoom(target, room):
    target.location = room

    if isinstance(target.tag,UserComponent):
        # -- PASTE DESCRIPTION --
        printRoomEntry(room)
        pausePlayer()

        # -- COMBAT CHECK --
        target.location.playerInRoom = True
        enemy = checkRoomForEnemies(room)
        if enemy != None:
            initCombat(target,enemy)
        room.enemy = None
        # -- ROOM ACTIONS UPDATE --
        roomLoop(target,room)



def roomLoop(player, room):
    
    printRoomIntroduction(room)
    pausePlayer()
    movedRoom = False
    while movedRoom == False:
        movedRoom = PlayerRoomChoiceAction().do(activator=player,target=room)

    #Player has moved room or signed that they are quitting the game
    if isinstance(movedRoom,Room):
        enterRoom(player,movedRoom)
    
    # Quit game
    if movedRoom == True:
        exit()

def assignNPCsToRoom(room):
    for npc in room.npcs:
        npc.location = room

def checkRoomForEnemies(room):
    if room.playerInRoom and room.enemy != None:
        return room.enemy
    else:
        return None
    
# For entering the room for the first time (before combat)
def printRoomEntry(room):
    printTitle(room.name)
    if room.descriptionComp != None:
        printSubTitle("Description")
        print(room.descriptionComp.value)
    printLine()

# For entering the room after the first time (or after combat)
def printRoomIntroduction(room):
    printTitle(room.name)
    if room.roomIntro != " ":
        print(room.roomIntro)
        
def addRoomConnection(room1: Room, room2: Room, lock:LockComponent = None):
    room1.connectedRooms.append(RoomConnectionComponent(otherRoom=room2, lock=lock))
    room2.connectedRooms.append(RoomConnectionComponent(otherRoom=room1, lock=lock))
    
