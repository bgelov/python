#https://docs.python.org/3/library/dataclasses.html
import calendar

mm,dd,yyyy = map(int, input().split())
weekdayNum = calendar.weekday(yyyy,mm,dd)
weekdayText = calendar.day_name[weekdayNum]
print(weekdayText.upper())