# Write a program to print the numbers between 1 and 10, along with an indication of whether each is even or odd

def evenOdd():
#	""" function to print the the if number is even or odd """
	for x in range(1,10):
		if x % 2 == 0:
			print x, "is even"
		else:
			print x, "is odd"

evenOdd()

#""" same program using map function """
print '#'*10 ,"using map function", '#'*10
def evenOdd(num):
	if num % 2 == 0:
		return str(num) + " is even"
	else:
		return str(num) + " is odd"

seq = list(map(evenOdd, range(0,10)))
for str1 in seq:
	print str1

#""" same program using list comprehension """
print '#'*10 ,"using list comprehension", '#'*10

#evn_seq = [str(x) + " is even" for x in range(0,10) if x % 2 == 0]
#odd_seq = [str(x) + " is odd" for x in range(0,10) if x % 2 != 0]
#seq = evn_seq + odd_seq

""" or """

seq = [str(x) + " is even" for x in range(0,10) if x % 2 == 0] + [str(x) + " is odd" for x in range(0,10) if x % 2 != 0]
seq.sort()

for x in seq:
	print x