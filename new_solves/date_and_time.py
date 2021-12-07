import datetime

# tday = datetime.date.today()
# tdelta = datetime.timedelta(days=7)

# dt = datetime.datetime(1994, 5, 21, 12, 30, 45, 10000)
dt = datetime.datetime.now().strftime('%B %d, %Y')
print(dt)