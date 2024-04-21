extends Node2D
class_name PilotSeatComponent

# ==========================
# == Pilot Seat Component ==
# ==========================
# - 


var occupied: bool = false
var enterAreaEntered: bool = false
var possiblePilot: Node2D
var truePilot: Node2D

func enter():
	print("Player Enters Tank")
	occupied = true
	print(possiblePilot.name)
	possiblePilot.enabled = false
	truePilot = possiblePilot

func exit():
	print("Player Exits Tank")
	print(truePilot.name)
	occupied = false
	truePilot.enabled = true


func _on_enter_area_body_entered(body: Node2D) -> void:
	if body is Player:
		enterAreaEntered = true
		possiblePilot = body
		print("player here")

func _on_enter_area_body_exited(body: Node2D) -> void:
	if body is Player:
		enterAreaEntered = false
		possiblePilot = null
		print("player left")
