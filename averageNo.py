# Write a program to compute the average of the ten numbers 1, 4, 9, ..., 81, 100, that is, the average of the squares of the numbers from 1 to 10

from squareNos import sq

msg = "is the average number of the ten numbers 1,4,9,...,81,100"

def calAverage():
	total = 0

	for x in range(11):
		total += sq(x)

	return total / 10.0

print calAverage(), msg

""" using map function """

seq = list(map(sq, range(0,11)))
print sum(seq)/10.0, msg

""" using list comprehension """

print sum([x ** 2 for x in range(11)])/10.0, msg
