extends Node
class_name MovementComponent
# Handles the movement of the entity. Calculates speed, direction, etc.

@export var MaxSpeed: float
@export var Acceleration: float 
var currentSpeed: float = 0.0

func get_speed(delta, velocity: Vector3):
	pass
