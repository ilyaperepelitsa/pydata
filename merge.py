from pandas import DataFrame
import pandas as pd
import numpy as np


df1 = DataFrame({"key" : ["b", "b", "a", "c", "a", "a", "b"],
                 "data1" : range(7)})

df2 = DataFrame({"key" : ["a", "b", "d"],
                 "data2" : range(3)})

df1
df2

pd.merge(df1, df2)
pd.merge(df1, df2, on = "key")

### when the key columns have different names

df3 = DataFrame({"lkey" : ["b", "b", "a", "c", "a", "a", "b"],
                 "data1" : range(7)})

df4 = DataFrame({"rkey" : ["a", "b", "d"],
                 "data2" : range(3)})

#inner join by default
pd.merge(df3, df4, left_on = "lkey", right_on = "rkey")
pd.merge(df1, df2, how = "outer")



df1 = DataFrame({"key" : ["b", "b", "a", "c", "a", "b"],
                 "data1" : range(6)})

df2 = DataFrame({"key" : ["a", "b", "a", "b", "d"],
                 "data2" : range(15, 20)})
df1
df2

pd.merge(df1, df2, on = "key", how = "left")
pd.merge(df1, df2, how = "inner")



left = DataFrame({"key1" : ["foo", "foo", "bar"],
                  "key2" : ["one", "two", "one"],
                  "lval" : [1, 2, 3]})

right = DataFrame({"key1" : ["foo", "foo", "bar", "bar"],
                   "key2" : ["one", "one", "one", "two"],
                   "rval" : [4, 5, 6, 7]})

pd.merge(left, right, on = ["key1", "key2"], how = "outer")

pd.merge(left, right, on = "key1")

left
right
pd.merge(left, right, on = "key1")
pd.merge(left, right, on = "key1", suffixes = ("_left", "_right"))


### JOINING ON INDEX

left1 = DataFrame({"key" : ["a", "b", "a", "a", "b", "c"],
                   "value" : range(6)})

right1 = DataFrame({"group_val" : [3.5, 7]},
                   index = ["a", "b"])
left1
right1

pd.merge(left1, right1, left_on = "key", right_index = True)
pd.merge(left1, right1, left_on = "key", right_index = True, how = "outer")



lefth = DataFrame({"key1" : ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada"],
                   "key2" : [2000, 2001, 2002, 2001, 2002],
                   "data" : np.arange(5.)})
righth = DataFrame(np.arange(12).reshape((6, 2)),
                    index = [["Nevada", "Nevada", "Ohio", "Ohio", "Ohio", "Ohio"],
                              [2001, 2000, 2000, 2000, 2001, 2002]],
                    columns = ["event1", "event2"])

lefth
righth

pd.merge(lefth, righth, left_on = ["key1", "key2"], right_index = True)
pd.merge(lefth, righth, left_on = ["key1", "key2"], right_index = True, how = "outer")


left2 = DataFrame([[1., 2.], [3., 4.], [5., 6.]],
                    index=['a', 'c', 'e'],
                    columns=['Ohio', 'Nevada'])

right2 = DataFrame([[7., 8.], [9., 10.], [11., 12.], [13, 14]],
                    index=['b', 'c', 'd', 'e'],
                    columns=['Missouri', 'Alabama'])

left2
right2
pd.merge(left2, right2, how='outer', left_index=True, right_index=True)


left2.join(right2, how = "outer")

left2

right2
another = DataFrame([[7, 8], [9, 10], [11, 12], [16, 17]],
                    index = ["a", "c", "e", "f"],
                    columns = ["New York", "Oregon"])

another
left2.join([right2, another])
left2.join([right2, another], how = "outer")
