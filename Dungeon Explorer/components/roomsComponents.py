from dataclasses import dataclass

@dataclass
class LockComponent:
    locked:bool = True
    key: object = None

@dataclass
class RoomConnectionComponent:
    otherRoom: object = None
    lock: LockComponent = None

    def __str__(self) -> str:
        return f"{self.otherRoom} {f' - Locked' if self.lock != None and self.lock.locked == True else ''}{f'(Needs {self.lock.key})' if self.lock != None and self.lock.key != None else ''}"
    
