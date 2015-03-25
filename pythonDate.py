# Program to convert string to date
import datetime

strDOB = "1990-07-24"

def strToDate(strDate, format='%Y-%m-%d'):
	
	ret_date = datetime.datetime.strptime(strDate, format)
	return ret_date;

def calculate_age(dob):
	""" Method to calculate the age of user from date of birth """
	present = datetime.date.today()
	age = present.year - dob.year - ((present.month, present.day) < (dob.month, dob.day))
	return age

# print "Date in string format : ", strDOB
# print "After strToDate : ", strToDate(strDOB)

print "User's Date of Birth : ", strDOB
print "User's Age : ", calculate_age(strToDate(strDOB))