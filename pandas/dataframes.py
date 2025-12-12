import pandas as pd

# DataFrames : 2D labeled data structure with 
#               columns of potentially 
#               different types simar to 
#               a spreadsheet or SQL table

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [24, 27, 22, 32],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston']
    }
df = pd.DataFrame(data,index=['E1', 'E2', 'E3', 'E4'])
print("DataFrame:\n", df)

# Accessing columns
print("Names Column:\n", df['Name'])

# Accessing rows by label
print("Row E2:\n", df.loc['E2'])
print("Row E3:\n", df.iloc[2])  # Accessing rows by position

# adding a new column
df['Salary'] = [70000, 80000, 60000, 90000]
print(df)

# adding a new row
new_row = {'Name': 'Eva', 'Age': 29, 'City': 'Miami', 'Salary': 75000}
df.loc['E5'] = new_row
print("After adding new row:\n", df)

new_row2 = pd.DataFrame({'Name': ['Frank'], 'Age': [33], 'City': ['Seattle'], 'Salary': [85000]}, index=['E6'])
df = pd.concat([df, new_row2])
print("After adding another new row:\n", df)

new_rows1 = pd.DataFrame({'Name': ['Grace', 'Hank'], 'Age': [26, 31], 'City': ['Boston', 'Denver'], 'Salary': [72000, 88000]}, index=['E7', 'E8'])
df = pd.concat([df, new_rows1])  
print("After adding multiple new rows:\n", df)
new_rows2 = pd.DataFrame([{'Name': 'Ivy', 'Age': 28, 'City': 'Austin', 'Salary': 78000},
                           {'Name': 'Jack', 'Age': 30, 'City': 'San Francisco', 'Salary': 95000}], index=['E9', 'E10'])
df = pd.concat([df, new_rows2])
print("After adding more new rows:\n", df)