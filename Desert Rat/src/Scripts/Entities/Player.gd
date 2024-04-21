extends CharacterBody2D
class_name Player

const speed = 200.0
const JUMP_VELOCITY = -400.0

# Get the gravity from the project settings to be synced with RigidBody nodes.
var gravity: int = ProjectSettings.get_setting("physics/2d/default_gravity")

var enabled: bool = true

func get_input():
	if enabled:
		var input_direction = Input.get_vector("left", "right", "up", "down")
		velocity = input_direction * speed

func _process(delta: float) -> void:
	if enabled:
		visible = true
	else:
		visible = false

func _physics_process(delta):
	get_input()
	move_and_slide()
