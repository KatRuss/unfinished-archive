extends Node2D
class_name TankHeadComponent

# =========================
# == Tank Head Component ==
# =========================
# - Handles the rotation and firing of the tank head.

# Component Nodes
@onready var pivot = $Pivot
@onready var shoot_cast: RayCast2D = $Pivot/ShootCast


# External Nodes
# - inventory/storage components for the shells

# Data Resources
@export var headData: TankHeadData
var ammo = 5

# Local Variables
var mouseAngle

func rotate_to_target(delta, target: Vector2):
	var rot = pivot.get_angle_to(target)
	pivot.rotation = lerp(pivot.rotation,rot+pivot.rotation,headData.rotateSpeed * delta)

func fireWeapon():
	if ammo > 0:
		if shoot_cast.is_colliding():
			print("Hit Something")
		else:
			print("Hit Nothing")
		ammo -= 1
	else:
		print("No ammo")
