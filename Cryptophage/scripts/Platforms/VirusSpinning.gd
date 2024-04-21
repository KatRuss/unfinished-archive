extends VirusPlatform

@export var rotateX: bool
@export var rotateY: bool
@export var rotateZ: bool
@export var spinSpeed: float
@export var reverse: bool

var direction: Vector3

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	direction = -Vector3(rotateX,rotateY,rotateZ).normalized() if reverse else Vector3(rotateX,rotateY,rotateZ).normalized()

	if direction != Vector3.ZERO:
		rotate_object_local(direction, delta * spinSpeed)
