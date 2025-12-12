import numpy as np

"""
Aggregate Functions : Summarize Data and Typically
 return a single value
"""
array = np.array([[1,2,3,4,5],
                  [6,7,8,9,10]])

print(np.sum(array))
print(np.mean(array))
print(np.std(array))
print(np.var(array))
print(np.min(array))
print(np.max(array))
print(np.argmin(array))  # Index of minimum value
print(np.argmax(array))  # Index of maximum value 
print(np.median(array))

print(np.sum(array, axis=0))  # Sum along columns
print(np.sum(array, axis=1))  # Sum along rows