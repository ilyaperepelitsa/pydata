import pandas as pd
import numpy as np
from pandas import DataFrame


data = DataFrame({'food':
                ['bacon', 'pulled pork', 'bacon', 'Pastrami',
                'corned beef', 'Bacon', 'pastrami', 'honey ham','nova lox'],
                'ounces': [4, 3, 12, 6, 7.5, 8, 3, 5, 6]})

data

meat_to_animal = { 'bacon': 'pig',
                    'pulled pork': 'pig',
                    'pastrami': 'cow',
                    'corned beef': 'cow',
                    'honey ham': 'pig',
                    'nova lox': 'salmon'}


data["animal"] = data["food"].map(str.lower).map(meat_to_animal)

data
data["food"].map(lambda x: meat_to_animal[x.lower()])
