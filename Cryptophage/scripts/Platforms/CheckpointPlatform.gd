extends Platform
class_name CheckpointPlatform

var playerHasEntered = false

func do_effect():
	playerHasEntered = true

func _on_player_enter_component_body_exited(body):
	if playerHasEntered:
		queue_free()
