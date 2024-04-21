extends Node
class_name Level_Master

@export var PlatformsHolder: Node
@export var numOfViruses: floatingInt
@export var numOfCores: floatingInt
@export var level_timer: floatingInt
@export var score_int: floatingInt
@export var end_point: ExitPlatform
@export var virusThreshold: int # Number of viruses that need to be popped before the level can be finished.
var level_over = false
var score = 0

@export var starting_time: int

func _ready():
	# TODO: Edit this so it includes viruses/cores that are nested in other nodes
	level_timer.currentNum = starting_time
	for platform in PlatformsHolder.get_children():
		if platform is VirusPlatform:
			numOfViruses.currentNum += 1
		if platform is CoreFilePlatform:
			numOfCores.currentNum += 1
	print("Num of Cores: " + str(numOfCores.currentNum))
	print("Num of Viruses: " + str(numOfViruses.currentNum))

func _process(delta):
	if numOfViruses.currentNum <= virusThreshold:
		set_level_completable()
	if level_timer.currentNum == 0:
		pass # Timeout, player loses

func set_level_completable():
	end_point.readyToGo = true

func calculate_score():
	score = (level_timer.currentNum/2 + (numOfCores.currentNum/2)) - numOfViruses.currentNum
	print(score)
	if score > score_int.currentNum:
		score_int.currentNum = score

func _on_timer_timeout():
	if not level_over:
		level_timer.currentNum -= 1

