# Python program to display calendar of given month of the year

# import module
import calendar
import datetime

now = datetime.datetime.now()
print(calendar.month(now.year, now.month))

