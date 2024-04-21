class ScreenAction:
    name: str = "Unamed Screen Action"
    
    def __str__(self) -> str:
        return self.name
    
    def do(self):
        return False

# -- Simple Screen Actions --
class QuitAppAction(ScreenAction):
    name = "Quit"
    
    def do(self):
        quit()

class TestAction(ScreenAction):
    name = "Say hi"
    
    def do(self):
        print("Hello!")
        return False

class ReturnAction(ScreenAction):
    name = "Return"
    def do(self):
        return True

class MoveScreenAction(ScreenAction):
    def __init__(self, target) -> None:
        self.name = f"Move to {target}"
        self.target = target
    
    def do(self):
        self.target.Show()
        return False
