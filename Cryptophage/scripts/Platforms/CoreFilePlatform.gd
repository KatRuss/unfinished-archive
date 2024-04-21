extends Platform
class_name CoreFilePlatform

var damaged = false
@export var damagedTimer: float
@export var HealthyColour: Color
@export var WarningColour: Color
@export var DamagedColour: Color

@onready var timer = $Timer
@onready var mesh = $MeshInstance3D

func _ready():
	mesh.mesh.material.albedo_color = HealthyColour

func do_effect():
	print("Get off the platform now.")
	mesh.mesh.material.albedo_color = WarningColour
	timer.start(damagedTimer)

func _on_player_enter_component_body_exited(body):
	timer.stop()
	if not damaged:
		mesh.mesh.material.albedo_color = HealthyColour
		
func _on_timer_timeout():
	damaged = true
	mesh.mesh.material.albedo_color = DamagedColour
	# Tell something that this file has been damaged

