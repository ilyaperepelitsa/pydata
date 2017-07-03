from datetime import datetime
import pandas as pd

stamp = datetime(2011, 1, 3)
str(stamp)

stamp.strftime("%Y-%m-%d")


value = "2011-01-03"
datetime.strptime(value, "%Y-%m-%d")
datetime(2011, 1, 3, 0, 0)

datestrs = ["7/6/2011", "8/6/2011"]
[datetime.strptime(x, "%m/%d/%Y") for x in datestrs]


#### parsing the shit

from dateutil.parser import parse

parse("2011-01-03")
parse('Jan 31, 1997 10:45 PM')
parse('6/12/2011', dayfirst=True)


datestrs
pd.to_datetime(datestrs)

idx = pd.to_datetime(datestrs + [None])
idx
pd.isnull(idx)
