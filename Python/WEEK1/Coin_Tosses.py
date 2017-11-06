
import random

def coin(x):
	if(x == 1.0):
		return "head"
	else:
		return "tail"

def coin_toss():
	heads=0
	tails=0
	print "Starting the program..."
	for num in range(1,5001):
		random_num = random.random()
		rounded = round(random_num)
		if(rounded == 1.0):
			heads+=1
		else:
			tails+=1
		print "Attempt #" + str(num) + ": Throwing a coin...It's a " + str(coin(rounded)) + "... Got " + str(heads) + " head(s) so far and " +str(tails) + " tail(s) so far"
	print "Ending the program, thank you!"
		


coin_toss()