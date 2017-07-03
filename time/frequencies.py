from pandas.tseries.offsets import Hour, Minute

pd.date_range('1/1/2000', '1/3/2000 23:59', freq='4h')
Hour(2) + Minute(30)
pd.date_range('1/1/2000', periods=10, freq='1h30min')
