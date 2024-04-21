# To create a universal function list to make sure text formatting is consistant
def printThinLine():
    print("............")

def printLine():
    print("------------")
    
def printTitle(title: str):
    print(f"=== {title} ===")
    
def printSubTitle(subtitle: str):
    print(f"--- {subtitle} ---")
    
def printListEntry(listEntry: str):
    print(f' - {listEntry}')