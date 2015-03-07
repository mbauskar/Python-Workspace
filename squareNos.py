# program to print the numbers from 1 to 10 and their square

def print_sq():
	""" function to print the number 1 to 10 and their square """
	print "Number\t", "Square"
	for x in range(11):
		print x, "\t", x ** 2

print "Using print_sq function"
print_sq()

print "using map function"
def sq(x): return x ** 2		# function to calculate square of number

print "Numbers",range(0,11)		# prints the list of range to 0, 10
print "Squares",list(map(sq, range(0,11))), "\n"	#using map function to calculate the square of numbers

print "Using list comprehensions"
print "Numbers",range(0,11)
print "Squares", [x ** 2 for x in range(11)], "\n"	# list comprehensions to calculate square of numbers
