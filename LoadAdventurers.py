# To scrape players and stats from baseball-reference
from lxml import html
import requests

def LoadAdventurers():


	adventurers = {"home": ["", "", "", "", "", "", ""], "away": ["", "", "", "", "", "", ""]}

	# Scrape names of top 8 batters
	for x in range(7):
		# Home
		adventurers["home"][x] = "bobo" + str(x)

		# Away
		adventurers["away"][x] = "bibi" + str(x)


	# Strike rates
	home_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.4]
	away_avg = [0.1, 0.2, 0.3, 0.4, 0.5, 0.7, 0.4]

	# Add batting averages to batters array
	adventurers["home"] = [
		[adventurers["home"][0], home_avg[0]],
		[adventurers["home"][1], home_avg[1]],
		[adventurers["home"][2], home_avg[2]],
		[adventurers["home"][3], home_avg[3]],
		[adventurers["home"][4], home_avg[4]],
		[adventurers["home"][5], home_avg[5]],
		[adventurers["home"][6], home_avg[6]],
	]
	adventurers["away"] = [
		[adventurers["away"][0], away_avg[0]],
		[adventurers["away"][1], away_avg[1]],
		[adventurers["away"][2], away_avg[2]],
		[adventurers["away"][3], away_avg[3]],
		[adventurers["away"][4], away_avg[4]],
		[adventurers["away"][5], away_avg[5]],
		[adventurers["away"][6], away_avg[6]],
	]


	# Sort array by batting average to determine batting order
	adventurers["home"] = sorted(adventurers["home"], key=lambda x: x[1], reverse=True)
	adventurers["away"] = sorted(adventurers["away"], key=lambda x: x[1], reverse=True)

	return adventurers
