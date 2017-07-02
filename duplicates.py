import pandas as pd
import numpy as np
from pandas import DataFrame

data = DataFrame({'k1': ['one'] * 3 + ['two'] * 4,
                  'k2': [1, 1, 2, 3, 3, 4, 4]})

data
data.duplicated()

data.drop_duplicates()
data["v1"] = range(7)
data
data.drop_duplicates()

data.drop_duplicates(["k1", "k2"], keep = "first")
