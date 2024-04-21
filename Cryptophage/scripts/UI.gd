extends Control

@export var level_timer: floatingInt
@export var level_label: Label

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	level_label.text = str(level_timer.currentNum)
