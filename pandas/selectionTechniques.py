import pandas as pd

df = pd.read_csv('data_csv.csv',index_col='id')

# Selecting a single column
names = df['first_name']
print("Names Column:\n", names)
email = df['email']
print("enail Column:\n", email)
gender = df['gender']
print("Gender Column:\n", gender)

# Selecting multiple columns
subset = df[['first_name', 'last_name', 'email']]
print("Subset of Columns:\n", subset)

# Selection by rows

print(df.loc[5])  # First row by label
print(df.iloc[1])  # Second row by position

# Selection by rows by index = id
print(df.loc[1])  # Row with index label 1
print(df.loc[4:7, ['first_name', 'email']])


print(df.iloc[2:15:3,0:3]) # Rows from index 2 to 14 with step 3 and first 4 columns