import numpy as np

# Scalar operations
a = np.array([1, 2, 3, 4, 5])

print("Original array:", a)
print("Array after addition of 2:", a + 2)
print("Array after multiplication by 3:", a * 3)
print("Array after squaring each element:", a ** 2)
print("Array after subtracting 2:", a - 2)
print("Array after dividing by 2:", a / 2)
print("Array after integer division by 2:", a // 2)
print("Array after modulo 2:", a % 2)

# Vector operations
b = np.array([1, 2, 3, 4, 5])
print(np.sqrt(b))
c = np.array([1.5,2.7,3.1,4.6,5.8])
print(np.floor(c))
print(np.ceil(c))
print(np.round(c))

#exercise
radii = np.array([1,2,3])

print("Areas of circles with given radii:", np.pi * radii**2)

# Exercise 2
array1 = np.array([10, 20, 30, 40, 50])
array2 = np.array([1, 2, 3, 4, 5])

print("Element-wise addition:", array1 + array2)
print("Element-wise subtraction:", array1 - array2)


# Comparision operations
scores = np.array([91, 85, 78, 92, 88,68,56,99,73,84])
print("Scores greater than or equal to 90:", scores >= 90)
print("Scores less than 80:", scores < 80)

scores[scores < 70] = 0
print("Scores after setting values less than 70 to 0:", scores)