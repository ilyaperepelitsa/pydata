from datetime import datetime
import numpy as np
import pandas as pd
from pandas import DataFrame
from pandas import Series
import pandas
import numpy

dates = [datetime(2011, 1, 2), datetime(2011, 1, 5),
        datetime(2011, 1, 7), datetime(2011, 1, 8),
        datetime(2011, 1, 10), datetime(2011, 1, 12)]

dates
ts = Series(np.random.randn(6), index = dates)
ts

ts.index
ts.index.dtype


### indexing

ts['1/10/2011']
longer_ts = Series(np.random.randn(1000),
                    index=pd.date_range('1/1/2000', periods=1000))

longer_ts
longer_ts['2001']
longer_ts['2001-05']
ts[datetime(2011, 1, 7):]
ts['1/6/2011':'1/11/2011']
ts.truncate(after='1/9/2011')
dates = pd.date_range('1/1/2000', periods=100, freq='W-WED')
long_df = DataFrame(np.random.randn(100, 4),
                        index=dates,
                        columns=['Colorado', 'Texas', 'New York', 'Ohio'])

long_df
long_df.ix['5-2001']



### duplicates

dates = pd.DatetimeIndex(['1/1/2000', '1/2/2000', '1/2/2000',
                            '1/2/2000', '1/3/2000'])

dup_ts = Series(np.arange(5), index=dates)
dup_ts
dup_ts.index.is_unique
grouped = dup_ts.groupby(level=0)

grouped.mean()
grouped.count()

#### frequencies and shifting
ts
ts.resample("D")

### date ranges
index = pd.date_range('4/1/2012', '6/1/2012')
index
pd.date_range(start='4/1/2012', periods=20)
pd.date_range(end='6/1/2012', periods=20)
pd.date_range('1/1/2000', '12/1/2000', freq='BM')
pd.date_range('5/2/2012 12:56:31', periods=5)
pd.date_range('5/2/2012 12:56:31', periods=5, normalize=True)
