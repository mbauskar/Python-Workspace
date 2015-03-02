#Program to find the primary number from 0 to n and store the result in file
import redirect
 
no = int(raw_input("Enter the positive number : "))

if no < 0:	#check if user enters -ve number
	print "You have entered -ve number"
elif no < 2:	#check if user enters the value less than 2
	print "there are no primary number upto %d"%(no)
else:
	primary_nos = []
	
	for i in range(2, no):
		for j in range(2, i/2 + 1):
			if i % j == 0:
				break
		else:
		# loop fell through without finding a factor
			primary_nos.append(i)

	with open('primary_numbers.txt','w') as myfile:
		with redirect.StdoutRedirect(myfile):
			print "Prime number between 0 to %d are : "%(no),
			print primary_nos
	
	print "Primary Numbers are stored in primary_number.txt file"
