import datetime
now = datetime.datetime.now()
day = datetime.date.isoweekday(now)
today = datetime.date.today()
print now
print now.day
print now.hour
print day
print today
print now.ctime()
