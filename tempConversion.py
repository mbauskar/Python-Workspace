# Program to print Farhenheit to celsius table for -40 to 200 degrees

def toCelsius(tempF):
	return ( 5.0 / 9.0) * (tempF - 32)	# converting temperature from farhenheit to celsius using fprmula F = 5/9 * (C - 32)

def toFahrenheit(tempC):
	return tempC * (9.0 / 5.0) + 32		# converting temperature from celsius to farhenheit using fprmula C = (9/5 * F) + 32

def celsiusToFarhenheit(minTemp, maxTemp):
	tempList = [t for t in range(minTemp, maxTemp + 1, 10)]		# get the list of temp in celsius in increments of 10
	for temp in tempList:
		print temp, "C =", toFahrenheit(temp), "F"

def farhenhietToCelsius(minTemp, maxTemp):
	tempList = [t for t in range(minTemp, maxTemp + 1, 10)]		# get the list of temp in celsius in increments of 10
	for temp in tempList:
		print temp,"F =", toCelsius(temp), "C"

print "\nDegree celsius to degree farhenheit conversion table"
celsiusToFarhenheit(10,40)
print "\nDegree farhenheit to degree celsius conversion table"
farhenhietToCelsius(50,100)