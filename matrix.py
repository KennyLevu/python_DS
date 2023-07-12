# matrix
# a python matrix is a 2d array, every element must be the same size
# use numpy package for matrix

import numpy as np

# defining a matrix
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])

print("\n Defining a 4x4 matrix")
print(a)

# np.reshape changes the shape of the array without changing it's data
# the total amount of elements must remain the same
print("\n Reshaing the matrix to a 2x8")
print("\n Reshaped matrices must retain the same amount of elements")
m = np.reshape(a,(2,8))
print(m)

# accessing elements
print("\n Acessing Elements")
print(a[1])
print(a[1][1])
print(a[1][1], a[2][0])

# adding elements
print("\n reshaping to 4x4")
m = np.reshape(a,(4,4))
print(m)
print("\n Adding elements to reshaped 4x4")
m = np.append(m,[[1, 15,13,11]],0)
print(m)

print("\n adding elements along vertical axis")
m = np.append(m, [[0],[0],[0],[0],[0]], 1)
print(m)

# deleting elements
print("\n deleting elements along horizontal axis")
m = np.delete(m,[-1],0)
print(m)

print("\n deleting column along vertical axis")
m = np.delete(m,[0],1)
print(m)

