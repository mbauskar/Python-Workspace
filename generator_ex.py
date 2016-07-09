#  ref http://stackoverflow.com/questions/16769902/finding-the-date-of-the-next-saturday

from datetime import datetime
from datetime import timedelta

def get_weekdays(startdate, enddate, weekday):
	"""
	@startdate: given date, in format '2013-05-25'
	@weekday: week day as a integer, between 0 (Monday) to 6 (Sunday)
	"""
	startdate = datetime.strptime(startdate, '%Y-%m-%d')
	enddate = datetime.strptime(enddate, '%Y-%m-%d')
	while startdate <= enddate:
		t = timedelta((7 + weekday - startdate.weekday()) % 7)
		if (startdate + t) <= enddate:
			nextdate = (startdate + t).strftime('%Y-%m-%d')
			startdate = datetime.strptime(nextdate, '%Y-%m-%d') + timedelta(days=1)
			yield nextdate
		else:
			raise StopIteration

if __name__== "__main__":
	print [date for date in get_weekdays("2016-04-01", "2017-03-31", 5)]