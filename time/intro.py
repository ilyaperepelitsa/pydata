from datetime import datetime

now = datetime.now()
now
now.year
now.month
now.day


delta = datetime(2011, 1, 7) - datetime(2008, 6, 24, 15)
delta
delta.days
delta.seconds



from datetime import timedelta

start = datetime(2011, 1, 7)

start + timedelta(12)
