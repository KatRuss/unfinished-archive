extends Platform
class_name ExitPlatform

@export var level_master: Level_Master
var readyToGo = false

func do_effect():
	if readyToGo:
		print("Player has completed the level")
		call_for_score()
	else:
		print("You still have viruses to destroy, mate!")

func call_for_score():
	level_master.calculate_score()
