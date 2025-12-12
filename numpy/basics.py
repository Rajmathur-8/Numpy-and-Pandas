import numpy as np

# my_list = [1,2,3,4,5]

# print("Original list:", my_list)

# array = np.array(my_list)
# print("Numpy array:", array)
# print(type(array))

# array = array * 2
# print("Array after multiplication by 2:", array)

# # multidimensional array
# array_2d = np.array([[1,2,3],
#                      [4,5,6],
#                      [7,8,9]])
# print("Dimensions in this array: ",array_2d.ndim)
# print("2D Numpy array:\n", array_2d)

# array_3d = np.array([[[1,2,3],[4,5,6],[7,8,9]],
#                      [[10,11,12],[13,14,15],[16,17,18]],
#                      [[19,20,21],[22,23,24],[25,26,27]]])

# print("Dimensions in this array: ",array_3d.ndim)
# print("2D Numpy array:\n", array_3d)
# print("Shape of 3D array:", array_3d.shape)
# print(array_3d[0,0,0])  # Accessing element at first block, first row, first column
# print(array_3d[1,2,2])  # Accessing element at second


# array = np.array([[['a','b','c'],['d','e','f'],['g','h','i']],
#                   [['j','k','l'],['m','n','o'],['p','q','r']],
#                   [['s','t','u'],['v','w','x'],['y','z','0']]])

# words = array[1,2,2] + array[0,0,0] + array[1,0,0]
# print("Concatenated word:", words)

# Slicing
array = np.array([[1,2,3,4],
                  [5,6,7,8],
                  [9,10,11,12],
                  [13,14,15,16]])

print(array[0:3:2])
print("-----------")
print(array[0:4:2])
print("-----------")
print(array[::-1])
#Selecting columns
print("-----------")
print(array[:,1:4])

print("-----------")
print(array[:,::2])
print("-----------")
print(array[:2,:2])