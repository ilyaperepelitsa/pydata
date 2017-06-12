import numpy as np

x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[6, 23], [-1, 7], [8, 9]])

x
y

x.dot(y)

np.dot(x, np.ones(3))


from numpy.linalg import inv, qr
X = np.random.randn(5, 5)
X
mat = X.T.dot(X)
mat
inv(mat)
