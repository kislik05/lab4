import datetime

now = datetime.datetime.now() - datetime.timedelta(days = 1)

print(now.strftime("%S"), "seconds")