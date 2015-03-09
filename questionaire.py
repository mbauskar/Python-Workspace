# program to count the ans from user according to the question suffix, if suffix is ##A then 
# count how many time user inputs Y and N for the same sufix

def printResult(result):
	print 'A : ', result['##A']
	print 'B : ', result['##B']
	print 'C : ', result['##C']
	print 'D : ', result['##D']

resultY = {}
resultN = {}
#quesAns = {}
#totalQue = 0

resultY = {key:0 for key in ["##A","##B","##C","##D"]}
resultN = {key:0 for key in ["##A","##B","##C","##D"]}

with open('ques.txt') as file:		# open a ques file containing the list of question
	#totalQue = file.readlines()
	#user_ans = []
	#file.seek(0)

	#QueCount = 1
	for line in file.readlines():	# loop to iterate through the lines 
		QueSuffix = line[line.find('#'):].rstrip()	# get the suffix from question and remove whitespaces using rstrip
		print line[0:line.find('#')], ":"			# print the question without suffux use find() to get the first index of #
		user_ip = raw_input()						# get input from user

		if (user_ip == "Y") | (user_ip == "y"):
			resultY[QueSuffix] += 1					# if user input is Y then increment the count in resultY disctionary
		elif (user_ip == 'N') | (user_ip == 'n'):
			resultN[QueSuffix] += 1					# if user input is N then increment the count in resultN disctionary
		#else:
		#	print "invalid input"

		#user_ans.append(user_ip)

#quesAns = {k:v for k,v in }

print "Stats for Ans Y"
printResult(resultY)
print "Stats for Ans N"
printResult(resultN)