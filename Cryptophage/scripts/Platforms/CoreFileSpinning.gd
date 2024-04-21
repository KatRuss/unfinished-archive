extends CoreFilePlatform

@export var rotateX: bool
@export var rotateY: bool
@export var rotateZ: bool
@export var spinSpeed: float
@export var reverse: bool

var direction: Vector3

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	direction = -Vector3(rotateX,rotateY,rotateZ) if reverse else Vector3(rotateX,rotateY,rotateZ)
	rotate_object_local(direction.normalized(), delta * spinSpeed)
