import numpy as np
from numpy.core.defchararray import multiply

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a[0], a[1], a[2])
a[0] = 5
print(a)

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)
print(b[0, 0], b[0, 1], b[1, 0])

aa = np.zeros((2,2))
print(aa)
bb = np.ones((1,2))
print(bb)
c = np.full((2,2), 7)
print(c)
d = np.eye(2)
print(d)
e = np.random.random((2,2))
print(e)

# Array Indexing

import numpy as np
a = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12]])
b = a[:2, 1:3]
print(b)
print(a[0,1])
b[0, 0] = 77
print(a[0,1])

# Array Indexing 

a = np.array([[1, 2, 3, 4], [5,6,7,8], [9,10,11,12]])
row_1 = a[1, : ]
row_2 = a[1:2, :]
print(row_1, row_1.shape)
print(row_2, row_2.shape)

col_1 = a[:, 1]
col_2 = a[:, 2]
print(col_1, col_1.shape)
print(col_2, col_2.shape)

# Array Indexing

a = np.array([[1,2], [3,4], [5,6]])
print(a[[0,1,2], [0,1,0]])
print(np.array([a[0,0], a[1,1], a[2,0]]))
print(a[[0,0], [1,1]])
print(np.array([a[0,1], a[0,1]]))

# Array Indexing

a = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
print(a)

b = np.array([0,2,0,1])
print(a[np.arange(4), b])
# a[[0 1 2 3] , [0,2,0,1]] => [a00 a12 a20 a31]

a[np.arange(4), b] += 10
print(a)

# Array Indexing 

a = np.array([[1,2], [3,4], [5,6]])

bool_idx = (a>2)

print(bool_idx)
print(a[bool_idx])
print(a[a>2])

# Array Indexing

x = np.array([1,2])
print(x.dtype)

x = np.array([1.0, 2.0])
print(x.dtype)

x = np.array([1,2], dtype=np.int64)
print(x.dtype)

# Cac thao tac tren array

x = np.array([[1,2], [3,4]], dtype=np.float64)
y = np.array([[5,6], [7,8]], dtype=np.float64)

print(x+y)
print(np.add(x,y))

print(x - y)
print(np.subtract(x,y))

print(x*y)
print(np.multiply(x,y))

print(x/y)
print(np.divide(x,y))

# Cac thao tac tren array

x = np.array([[1,2], [3,4]])
y = np.array([[5,6], [7,8]])

v = np.array([9,10])
w = np.array([11,12])

print(v.dot(w))
print(np.dot(x,w))

print(x.dot(v))
print(np.dot(x,v).shape)

print(x.dot(y))
print(np.dot(x,y))


# Cac thao tac tren Array

x = np.array([[1,2,3], [3,4,5]])

print(np.sum(x))
print(np.sum(x, axis=0))
print(np.sum(x, axis=1))
# axis = 0 -> cot, axis = 1 -> hang

# Cac thao tac tren array
# Ma tran nghich dao

x = np.array([[1,2], [3,4]])

print(x)
print(x.T)

v = np.array([1,2,3])
print(v)
print(v.T)

# Cac thao tac tren array

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
y = np.empty_like(x) # tao matrix empty co so chieu giong x

for i in range(4):
    y[i, :] = x[i, :] +v
print(y)

# Cac thao tac tren array

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
vv = np.tile(v,(4,1)) # Xếp chồng 4 bản sao của v lên nhau

print(vv)

vv2 = np.tile(v, (4,2)) # Xếp chồng 4 bản sao của v v lên nhau
print(vv2)
y = x + vv
print(y)

x = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]])
v = np.array([1,0,1])
print(v+x)

# Cac thao tac tren array

v = np.array([1,2,3])
w = np.array([4,5])

x = np.array([[1,2,3], [4,5,6]])
print(x + v)
print((x.T + w).T)
print(x*2)