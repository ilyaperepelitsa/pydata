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






points = np.arange(-5, 5, 0.01)
xs, ys = np.meshgrid(points, points)

ys


import matplotlib.pyplot as plt
z = np.sqrt(xs ** 2 + ys ** 2)
z


plt.imshow(z, cmap = plt.cm.gray)
plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
plt.show()




### conditional logic as array operator


xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])


result = [(x if c else y)
            for x, y, c in zip(xarr, yarr, cond)]


result

### more concise version
result = np.where(cond, xarr, yarr)
result



###

arr = np.random.randn(4, 4)
arr
np.where(arr > 0, 2, -2)

np.where(arr > 0, 2, arr) # set only positive vals to 2


result = []
for i in range(n):
    if cond1[i] and cond2[i]:
        result.append(0)
    elif cond1[i]:
        result.append(1)
    elif cond2[i]:
        result.append(2)
    else:
        result.append(3)

# convert this BS into a nested where expression
np.where(cond1 & cond2, 0,
            np.where(cond1, 1,
                        np.where(cond2, 2, 3)))



arr = np.random.randn(5, 4)
arr.mean()
np.mean(arr)


arr.sum()
arr
arr.mean(axis = 1)

arr.sum(1)
arr.sum(0)



arr = np.array([1, 2, 3, 4, 5, 6])
arr.cumsum()
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
arr.cumsum(1)



### boolean arrays

arr = np.random.randn(100)
arr
(arr > 0).sum()


### sorting

arr = np.random.randn(8)
arr
arr.sort()
arr


arr = np.random.randn(5, 3)
arr
arr.sort(0)
arr


large_arr = np.random.randn(1000)
large_arr.sort()
large_arr

large_arr[int(0.05 * len(large_arr))]



###uniques and other

names = np.array(["Bob", "Joe", "Will", "Bob", "Will", "Joe", "Joe"])
np.unique(names)


ints = np.array([3, 3, 3, 2, 2, 1, 1, 4, 4])
np.unique(ints)


sorted(set(names))

### testing cross-membership

values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6])


np.unique(values)
np.intersect1d(values, [2, 5])
np.union1d(values, [22, 3])
np.in1d(values, [22, 3])
values[np.in1d(values, [22, 3])]
np.setdiff1d(values, [22, 3])

## ekements that are in either but not in both
np.setxor1d(values, [22, 3])
