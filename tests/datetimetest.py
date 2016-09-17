import datetime, time
day = datetime.datetime.now()
day = datetime.date.isoweekday(day)
today = datetime.date.today()
print day
print today
now = time.localtime()
t = time.strftime('%H:%M', now)
print t
n = datetime.datetime.now()
print n.hour, n.minute
