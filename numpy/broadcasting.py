import numpy as np

"""
Broadcasting allows NumPy to perform operations on
 arrays of different shapes in a way that 
 makes sense mathematically by virtually expanding 
 the smaller array so they can match in shape.
"""

array1 = np.array([[1,2,3,4]])
array2 = np.array([[1],[2],[3], [4]])

print(array1.shape)
print(array2.shape)

# Broadcasting in action
print(array1*array2)