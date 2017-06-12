import numpy as np

samples = np.random.normal(size = (4, 4))
samples


np.random.normal(size = 1000000)
np.random.seed(1)
np.random.randint(0, 2, size = (4, 4))



### random walks
# using standard library

import random
position = 0
walk = [position]
steps = 1000
for x in range(steps):
    step = 1 if random.randint(0, 1) else -1
    position += step
    walk.append(position)


## using numpy

nsteps = 1000
draws = np.random.randint(0, 2, size = nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
walk.min()
walk.max()

(np.abs(walk) >= 10).argmax()


### many walks
nwalks = 5000
nsteps = 1000
draws = np.random.randint(0, 2, size = (nwalks, nsteps))
steps = np.where(draws > 0, 1, -1)
walks = steps.cumsum(1)
walks.max()
walks.min()


hits30 = (np.abs(walks) >= 30).any(1)
hits30
hits30.sum()
