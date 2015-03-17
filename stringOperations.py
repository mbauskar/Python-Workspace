# Program to perform operations on string

def addCommasToNumericString(numStr):
	# Program to add the commas to numeric string e.g. numStr = 100000
	# Then the function must return 1,00,000

	inputList = list(numStr)
	inputList = inputList[::-1]			 
	numList = []						# list to store the final result
	commaAfterCount = 3					# count variable to traverse three times then add comma
	count = 0 							

	for num in inputList:				# converting numeric string to list and traversing the list in reverse order		
		if commaAfterCount == count:
			numList.append(',')			# adding the comma to numeric number
			commaAfterCount = 2			# As we will need second comma after each two numbers
			count = 0 					# setting count to zero

		numList.append(num)
		count += 1

	print listToString(numList[::-1])

def listToString(inputList):
	opStr = ""
	for ch in inputList:
		opStr += ch
	return opStr

print addCommasToNumericString("123456789")