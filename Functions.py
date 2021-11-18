import time
import math

def wait():  # Change both wait times to 0 for game to complete immediately
	time.sleep(2)  # default 2

def wait_short():
	time.sleep(.5)  # default .5

def format_strike_rate(avg):
	avg_string = str(avg)
	return avg_string
