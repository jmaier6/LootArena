# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 14:57:29 2021

@author: jmaier
"""
import random

def calculate_attack_outcome(attack_number, redo_pitch, edge_pos, margin, redo_attack_loops): #Needs cleanup

	# This function attempts to replicate real-world outcomes as accurately as possible.
	# Probability data was taken from this post:
	# https://www.baseball-fever.com/forum/general-baseball/statistics-analysis-sabermetrics/81427-pitch-outcome-distribution-over-25-years
	# Pitches 1-12 of each at bat match the probability data.
	# If pitch 13 is reached, there is no foul outcome, to help prevent infinite at-bats.

	# For each pitch, a random number between from 1 to 100 is generated. That number is used to determine the pitch outcome.
	# If the pitcher has the "edge", and the outcome is a ball or a ball in play (or vice versa), a second random number from 1 to 100 is generated.
	# If the second random number is between 0 and the edge %, the pitch outcome is disregarded and starts over.

	# So, if the pitcher has a 20% edge over the batter, and the initial outcome was a ball, there is a 20% chance of a do-over.

	rand = random.randint(1, 100)

	if attack_number == 1:
		if rand >= 1 and rand <= 43:  # Ball
			if edge_pos == "Attacker":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_attack_loops += 1
					return calculate_attack_outcome(attack_number, True, edge_pos, margin, redo_attack_loops)
				else:
					return "Miss"
			else:
				return "Miss"
		elif rand >= 44 and rand <= 72:  # Called Strike
			if edge_pos == "Attackee":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_attack_loops += 1
					return calculate_attack_outcome(attack_number, True, edge_pos, margin, redo_attack_loops)
				else:
					return "Hit"
			else:
				return "Hit"
		elif rand >= 73 and rand <= 82:  # Foul
			if edge_pos == "Attackee":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_attack_loops += 1
					return calculate_attack_outcome(attack_number, True, edge_pos, margin, redo_attack_loops)
				else:
					return "Critical Hit!"
			else:
				return "Critical Hit!"
		elif rand <= 83 and rand <= 88:  # Swinging Strike
			if edge_pos == "Attackee":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_attack_loops += 1
					return calculate_attack_outcome(attack_number, True, edge_pos, margin, redo_attack_loops)
				else:
					return "Hit"
			else:
				return "Hit"
		else:  # Ball in play
			if edge_pos == "Attacker":
				rand = random.randint(1, 100)
				if 1 <= rand <= round(margin, 0):  # Do-over?
					redo_attack_loops += 1
					return calculate_attack_outcome(attack_number, True, edge_pos, margin, redo_attack_loops)
				else:
					return "Ball_in_play"
			else:
				return "Ball_in_play"
	