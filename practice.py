import numpy as np


data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)


arr1


data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)


arr2
arr2.ndim
arr2.shape
arr1.dtype
arr2.dtype
np.zeros(10)
np.zeros((3, 6)) # passing a tuple for the shape


np.empty((2, 3, 2))


np.arange(20)


arr1 = np.array([1, 2, 3], dtype = np.float64)
arr2 = np.array([1, 2, 3], dtype = np.int32)
arr1.dtype
arr2.dtype



# converting types

arr = np.array([1, 2, 3, 4, 5])
arr.dtype
float_arr = arr.astype(np.float64)

float_arr.dtype

arr
float_arr


# decimal point t
arr = np.array([3.7, -1.2, -2.6, 0.5, 12.9, 10.1])
arr.astype(np.int32)


## strings to numeric

numeric_s = np.array(["-12.5", "6.9", "0.5"], dtype = np.string_)
numeric_s.astype(float)
numeric_s.astype(np.float64)



# using another as reference

int_array = np.arange(10)
calibers = np.array([0.22, 0.1, 0.007], dtype = np.float64)
int_array.astype(calibers.dtype)



### array operation

arr = np.array([[1, 2, 3], [4, 5, 6]])
arr
arr * arr
arr - arr


arr = np.arange(10)
arr
arr[5]
arr[5:8]
arr[5:8] = 12

arr



#slicing changes original array
arr_slice = arr[5:8]
arr_slice[1] = 12345
arr
arr_slice[:] = 64
arr


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr2d[2]
arr2d[0][2]


arr2d[:2]
arr2d[:2, 1:]



#### boolean indexing

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
data = np.random.randn(7, 4)
# data

names

names == "Bob"
data[names == "Bob"]
data[names == "Bob", 2:]
data[names == "Bob", 2]


data[names != "Bob"]
data[~(names == "Bob")]


(names == "Bob") | (names == "Will")

data[(names == "Bob") | (names == "Will")]
data[data < 0] = 0
data


data[names != "Joe"] = 7
data


arr = np.empty((8, 4))
arr
for i in range(8):
    arr[i] = i

arr

arr[[4, 3, 0, 6]]


arr = np.arange(32).reshape((8, 4))
arr
arr[[1, 5], [0, 3]]
arr[[1, 5, 7, 2], [0, 3, 1, 2]]
arr[[1, 5]]


arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]


arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])]




### transposing arrays

arr = np.arange(15).reshape((3, 5))
arr

arr.T



arr = np.random.randn(6, 3)
arr


np.dot(arr.T, arr)


arr = np.arange(16).reshape((2, 2, 4))
arr
arr.swapaxes(1, 2)



arr = np.arange(10)
np.sqrt(arr)

np.exp(arr)


x = np.random.randn(8)
x

pew = np.random.randn(3) * 3
pew
np.modf(pew)
