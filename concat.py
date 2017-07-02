import pandas as pd
from pandas import DataFrame
import numpy as np


df1 = DataFrame(np.arange(6).reshape(3, 2), index = ["a", "b", "c"],
                    columns = ["one", "two"])

df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index = ["a", "c"],
                    columns = ["three", "four"])

df1
df2


pd.concat([df1, df2], axis = 1, keys = ["level1", "level2"])
pd.concat({"level1" : df1, "level2" : df2}, axis = 1)


df1 = DataFrame(np.random.randn(3, 4), columns=['a', 'b', 'c', 'd'])
df2 = DataFrame(np.random.randn(2, 3), columns=['b', 'd', 'a'])

pd.concat([df1, df2], ignore_index=True)
