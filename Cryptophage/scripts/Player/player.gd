extends CharacterBody3D
class_name Player
# Player Movement Vars
@export var max_speed: float = 15.0
@export var ground_jump_velocity: float = 15.0
@export var double_jump_velocity: float = 8.0
@export var stomp_recovery_jump_velocity: float = 6.0

@export var Acceleration: float = 50.0
@onready var twist_pivot = $CameraSystem/TwistPivot

var current_speed = 0.0
var can_double_jump = true
var fall = 0.0
# Get the gravity from the project settings to be synced with RigidBody nodes.
var normal_fall = ProjectSettings.get_setting("physics/3d/default_gravity")
var double_fall = normal_fall / 1.5
var drop_fall = normal_fall * 6 # For when the player butt stomps
var drop_revocery_fall = normal_fall / 1.2
var isStomping = false

func set_speed(delta, current_speed: float, direction: Vector3) -> float:
	var f = max_speed if direction else 0.0
	return lerp(current_speed,f,delta * Acceleration)

func jump(jump_vel):
	velocity.y = jump_vel

func _physics_process(delta):
	# Add the gravity.
	if not is_on_floor():
		if isStomping:
			fall = drop_fall
		else:
			if Input.is_action_pressed("stomp"):
				isStomping = true
			else:
				fall = normal_fall if can_double_jump else double_fall
		velocity.y -= fall * delta
	
	# Handle jump.
	if Input.is_action_just_pressed("jump"):
		if is_on_floor():
			jump(ground_jump_velocity)

		elif can_double_jump:
			if isStomping:
				print("stomp recovery")
				isStomping = false
				fall = drop_revocery_fall
				jump(stomp_recovery_jump_velocity)
			else:
				jump(double_jump_velocity)
			can_double_jump = false

			
	
	if is_on_floor():
		can_double_jump = true
		isStomping = false
	
	# Get input
	var input_dir = Input.get_vector("mov_left", "mov_right", "mov_up", "mov_down")
	var direction = twist_pivot.basis * Vector3(input_dir.x, 0, input_dir.y).normalized()
	
	# Get Speed
	current_speed = set_speed(delta, current_speed, direction)
	
	velocity.x = move_toward(velocity.x, direction.x * current_speed, delta * Acceleration)
	velocity.z = move_toward(velocity.z, direction.z * current_speed, delta * Acceleration)
	
	move_and_slide()


func die():
	%Mesh.hide()	
	# Have something to respawn



