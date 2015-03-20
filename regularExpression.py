import re

def findNReplace(userDict,userString):
	# Function to find the pattern the string and replace it with another string
	#pattern = re.compile(r"(?<=\[])(.*?)(?=\])")

	print userString
	print userDict

	for key in re.findall(r"(?<=\[)(.*?)(?=\])",userString):
		old = "["+key+"]"
		new = str(userDict[key])
		
		userString = userString.replace(old, new)

	return userString

userDict = {'fname':'Makarand','lname':'Bauskar'}

print findNReplace(userDict, "My Name is [fname] [lname]")