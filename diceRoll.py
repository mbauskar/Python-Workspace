# Program count how often each roll come up while rolling pair of dice

import random

rollCount = {k:0 for k in range(2,13)}		# disctionary for roll counting

for n in range(100):
	dice1 = random.randint(1,6) 			# returns the random int value such that min <= no <= 6
	dice2 = random.randint(1,6) 			# we will consider this numbers is rolled by dice for dice 1 & dice 2

	rollCount[dice1 + dice2] += 1 			# incrementing the rollCount to its resp. roll

print "\nDice rolling count"

for k,v in sorted(rollCount.items()):
	print k, " is rolled", v, "times"

print "\nGraphical representation"

for k,v in sorted(rollCount.items()):
	prefix = ""
	if k < 10:
		prefix = "0"
	else:
		prefix = ""
	
	print prefix + str(k), ':', '*' * v