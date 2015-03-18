# Program to perform operations on string

"""
def addCommasToNumericString(numStr):
	# Program to add the commas to numeric string e.g. numStr = 100000
	# Then the function must return 1,00,000

	inputList = list(numStr)			# converting numeric string to list
	inputList = inputList[::-1]			# list in reverse order 
	numList = []						# list to store the final result
	commaAfterCount = 3					# count variable to traverse three times then add comma
	count = 0 							

	for num in inputList:						
		if commaAfterCount == count:
			numList.append(',')			# adding the comma to numeric number
			commaAfterCount = 2			# As we will need second comma after each two numbers
			count = 0 					# setting count to zero

		numList.append(num)
		count += 1

	return listToString(numList[::-1])
"""

# OR

def addCommasToNumericString(numStr):
	inputList =  list(numStr.split(".")[0])

	if len(inputList) > 3:
		sufix = [","] +	inputList[-3:]				# adding comma  before last three digits, 
													# inputList[-3:] returns last three digits

		inputList = inputList[:-3]					# updating inputList so we can add comma after each 2 digit

		for i in range(len(inputList))[::-2][1:]:	
			inputList.insert(i+1, ",")

		inputList += sufix							# adding sufix i.e last 3 digits to inputList

		return "".join(inputList)+"."+numStr.split(".")[1]
	else:
		return numStr

def addCommasToNumericString(numStr, format):
	# Function to add commas in numeric string using format
	sufix = []

	if numStr.find(".") != -1:
		inputList =  list(numStr.split(".")[0])		# if numeric string contains decimal point then
		sufix = ['.'] + list(numStr.split(".")[1])	# we will store the string after decimal point in suffix
	else:
		inputList = list(numStr)

	if len(inputList) > 3:
		commaAfterCount = 0
		if format == "INR":
			sufix = [","] +	inputList[-3:]	+ sufix	# adding comma  before last three digits, 
													# inputList[-3:] returns last three digits
			inputList = inputList[:-3]				# updating inputList so we can add comma after each 2 digit
			commaAfterCount = 2
		
		elif format == "USD":
			commaAfterCount = 3
			#or
			#return "{:,}".format(int(numStr))

		for i in range(len(inputList))[::-commaAfterCount][1:]:	
			inputList.insert(i+1, ",")

		inputList += sufix							# adding sufix i.e last 3 digits to inputList

		return "".join(inputList)#+"."+numStr.split(".")[1]
	else:
		return numStr

def listToString(inputList):
	opStr = ""
	for ch in inputList:
		opStr += ch						# Appending the character to string
	return opStr

print addCommasToNumericString("123456789.00","USD")