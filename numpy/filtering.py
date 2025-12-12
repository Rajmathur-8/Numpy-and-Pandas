import numpy as np

"""
Filtering : Filtering allows you to extract elements 
from an array based on 
certain conditions or criteria.
"""

ages = np.array([[21, 17, 20, 16, 18, 65, 35, 15],
                 [39 ,20 ,15 ,99 ,18 ,19 ,20 ,21]])

teens = ages[ages < 18]
print("Ages less than 18:", teens)

adults = ages[(ages >= 18) & (ages < 65)]
print("Ages between 18 and 65:", adults)

seniors = ages[ages >= 65]
print("Ages 65 and older:", seniors)

evens = ages[ages % 2 == 0]
print("Even ages:", evens)
odds = ages[ages % 2 != 0]
print("Odd ages:", odds)

# using Where function
adults = np.where(ages >= 18, ages, -1)
print("Adults with -1 for non-adults:\n", adults)
pass_fail = np.array([55, 67, 45, 89, 76, 38, 90, 72])
results = np.where(pass_fail >= 50, "Pass", "Fail")
print("Pass/Fail results:", results)