extends StaticBody3D
class_name Platform

func do_effect():
	print("Thing has been done!")

func _on_player_enter_component_body_entered(body):
	if body is Player:
		do_effect()
