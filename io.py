import numpy as np

arr = np.arange(10)
np.save("some_array", arr)


# loading

np.load("some_array.npy")


### save multiple arrays

np.savez("array_archive.npz", a = arr, b = arr)
arch = np.load("array_archive.npz")

arch
arch["a"]


np.savetxt("array.txt", arr, delimiter = ",")
pew = np.loadtxt("array.txt", delimiter = ",")
pew

# genfromtxt - structured arrays and missing data handling
