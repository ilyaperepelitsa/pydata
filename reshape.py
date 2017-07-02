import pandas as pd
from pandas import DataFrame
import numpy as np


data = DataFrame(np.arange(6).reshape((2, 3)),
                    index = pd.Index(['Ohio', 'Colorado'], name='state'),
                    columns = pd.Index(['one', 'two', 'three'], name='number'))

data

result = data.stack()
result
result.unstack()
result.unstack(0)
result.unstack("state")


df = DataFrame({'left': result, 'right': result + 5},
                columns=pd.Index(['left', 'right'],
                name='side'))
df

df.unstack("state")
df.unstack("state").stack("side")
df.stack("side")



## long to wide
pivoted = ldata.pivot('date', 'item', 'value')
