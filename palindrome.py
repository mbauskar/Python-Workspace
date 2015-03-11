# program to check if given number or string is palindrome or not

def palindromeNumber(number):
	no = number
	revNumber = 0

	while no != 0:
		revNumber *= 10
		revNumber += no % 10
		no = no / 10

	if revNumber == number:
		return True
	else:
		return False

def palindromeString(usrStr):
	revStr = usrStr[::-1]
	if revStr == usrStr:
		return True
	else:
		return False

number = raw_input("Enter the number : ")
if palindromeNumber(int(number)):
	print number, "is palindrome number"
else:
	print number, "is not palindrome number"

usrStr = raw_input("Enter the string : ")
if palindromeString(usrStr):
	print usrStr, "is palindrome string"
else:
	print usrStr, "is not palindrome number"