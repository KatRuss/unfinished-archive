extends Node3D


@export var speed: float = 0.05
var path: Path3D

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _ready():
	path = get_child(0)

func _process(delta):
	for follower in path.get_children():
		if follower is PathFollow3D:
			follower.progress_ratio += delta * speed
