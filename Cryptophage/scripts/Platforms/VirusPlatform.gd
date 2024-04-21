extends Platform
class_name VirusPlatform

@export var destroyTimer: float
@onready var timer = $Timer
@export var virusTotal: floatingInt

func do_effect():
	print("Virus has been done!")
	timer.start(destroyTimer)

func _on_timer_timeout():
	virusTotal.currentNum -= 1
	queue_free()
