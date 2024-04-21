extends CharacterBody2D
class_name Tank

# ===================
# == Tank Controls ==
# ===================
# - Handles the player controls and AI of a given tank, depending on what is currently piloting the tank



# Tank Body Stats - Could be replaced with a Tank Body Component
@export var bodyStats: TankBodyData
@export var tankHead: TankHeadComponent
@export var pilotSeat: PilotSeatComponent

var rotation_direction = 0
var speed: float = 0.0

# General Tank Controls
func get_input(delta):
	
	if pilotSeat:

		if Input.is_action_just_pressed("action") && pilotSeat.occupied:
			pilotSeat.exit()

		# Allow Player to enter tank
		if Input.is_action_just_pressed("action") && pilotSeat.enterAreaEntered:
			pilotSeat.enter()
			
		# Player Tank Controls
		if pilotSeat.occupied:
			if Input.is_action_just_pressed("fire") && tankHead:
				tankHead.fireWeapon()



			# Movement
			rotation_direction = Input.get_axis("left", "right")
			var throttle = Input.get_axis("down","up")

			if rotation_direction == 0:
				if throttle == 1:
					speed = lerpf(speed,bodyStats.maxForSpeed,bodyStats.acceleration * delta)
				if throttle == -1:
					speed = lerpf(speed,-bodyStats.maxRevSpeed,bodyStats.deceleration * delta)
				if throttle == 0:
					speed = lerpf(speed,0,bodyStats.falloff * delta)
			else:
				speed = lerpf(speed,0,bodyStats.falloff * delta)

			velocity = transform.x * speed

			# Tank Head Rotation
			if tankHead:
				tankHead.rotate_to_target(delta,get_global_mouse_position()) # basic rotator

func _physics_process(delta):
	get_input(delta)
	rotation += rotation_direction * bodyStats.rotation_speed * delta
	move_and_slide()
