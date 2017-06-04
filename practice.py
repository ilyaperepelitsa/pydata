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
