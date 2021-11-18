from lxml import html
import requests

def GetUserInputs():

	guild1_error = True
	while guild1_error == True:
		guild1 = input("Enter the name of the home guild: ")
		guild1_error = False

	guild2_error = True
	while guild2_error == True:
		guild2 = input("Enter the name of the away guild: ")
		guild2_error = False
	inputsArray = [guild1, guild2]
	return inputsArray
