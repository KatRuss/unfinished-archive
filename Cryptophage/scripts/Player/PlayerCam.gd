extends Camera3D

@onready var twist_pivot = $"../.."
@onready var pitch_pivot = $".."

# Temporary mouse vars
@export var mouse_sensitivity := 0.001
@export var x_clamp_bottom := 0.5
@export var x_clamp_top := 0.8

func _ready():
	Input.set_mouse_mode(Input.MOUSE_MODE_CAPTURED)

func _unhandled_input(event):
	if event is InputEventMouseMotion:
		if Input.get_mouse_mode() == Input.MOUSE_MODE_CAPTURED:
			twist_pivot.rotate_y(-event.relative.x * mouse_sensitivity)
			pitch_pivot.rotate_x(-event.relative.y * mouse_sensitivity) 
			pitch_pivot.rotation.x = clamp(
				pitch_pivot.rotation.x,
				-x_clamp_top,
				x_clamp_bottom
			)
