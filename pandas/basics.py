import pandas as pd
print(pd.__version__)

# Series creation
# Series : 1D labeled array capable of holding any data type
data = [10, 20, 30, 40, 50, 60]

series = pd.Series(data,index=['a', 'b', 'c', 'd', 'e', 'f'])
print("Series:", series)

print(series.loc['b'])  # Accessing element by label
print(series.iloc[2])   # Accessing element by position

print(series[series > 30])  # Conditional filtering

calories = {'day1': 1750, 'day2': 2100, 'day3': 1700}
series2 = pd.Series(calories)
print("Series from dict:", series2)

print(series2['day2'])  # Accessing element by key

series2.loc['day3'] += 200  # Modifying element
print(series2['day3'])

print(series2[series2 < 2000])  # Conditional filtering
print(series2[series2 > 2000])