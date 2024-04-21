from systems.playerCreatorSystem import playerCreator
from data.rooms import testRoom, combatRoom, lockedRoom
from systems.roomSystem import enterRoom,addRoomConnection,LockComponent

player = playerCreator()
addRoomConnection(testRoom,combatRoom)
addRoomConnection(combatRoom, lockedRoom,lock=LockComponent(True,None))

enterRoom(player,testRoom)