#Write a program to print the first 7 positive integers and their factorials

def factorial():
	print "factorial of 0 is 1"
	print "factorial of 1 is 1"
	
	for x in range(2,8):
		fact = 1
		for n in range(1, x+1):
			fact *= n

		print "factorial of", x, "is", fact

factorial()

# factorial using recursion function
print ""
print '*' * 10, "using recursive function", '*' * 10
print ""

def factorial(n):
	if n == 1:
		return 1
	else:
		return n * factorial(n-1)

for x in range(1,8):
	print "factorial of " + str(x) + "! is ", factorial(x)