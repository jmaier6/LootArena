import random
import time
import math
from datetime import datetime

##import Functions
from LA_userinputs import *
from LoadAdventurers import *
from Functions import *
from CalculateAttackOutcome import *

# Program start

print("Welcome to the Loot Arena!")

# Get user inputs to choose teams
inputs = GetUserInputs()
guilds = {"home": inputs[0], "away": inputs[1]}
print("")
print("This battle is between {} and {}.".format(inputs[0], inputs[1]))

print("")
print("Loading Adventurers...")

# Load players
adventurers = LoadAdventurers()

print("")
print("Adventurers Loaded")

# Print sorted batters for Home
print("\nIntroducing" + " " + guilds["home"] + ":")
wait()
for x in adventurers["home"]:
	print(x[0] + " - " + format_strike_rate(x[1]))
	wait_short()

# Print sorted batters for Away
print("Introducing"  + " " + guilds["away"] + ":")
wait()
for x in adventurers["away"]:
	print(x[0] + " - " + format_strike_rate(x[1]))
	wait_short()

wait()
print("")
wait()
print("ADVENTURERS! Are you ready to compete?")
wait()
print("ADVENTURERS! Are you ready to fight for glory?")
wait()
print("LET")
wait()
print("THE")
wait()
print("GAMES")
wait()
print("BEGIN!")
wait()
print("")
wait()
print("\033[1;93;40m" + adventurers["home"][0][0] + "\033[0m makes the first move for " + guilds["home"] + ".")
wait()
print()
wait()

status()

while gameover == False:  # Main game loop
    attack_result = calculate_attack_outcome(atbat_pitch_count, False, edge_pos, margin, redo_pitch_loops)
    gameover==True
