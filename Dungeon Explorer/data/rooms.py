from entities.room import Room
from components.baseComponents import DescriptionComponent
from data.enemies import *

combatRoom = Room(
    name="Test Combat Room",
    enemy=Goblin,
    descriptionComp=DescriptionComponent("This is a cool looking test room."),
    roomIntro="This is still a cool looking test room",
    connectedRooms=[]
)

testRoom = Room (
    name="Test Room",
    descriptionComp=DescriptionComponent("This is a test room"),
    roomIntro="It looks pretty cool",
    connectedRooms=[]
)

lockedRoom = Room(
    name="Locked Room",
)