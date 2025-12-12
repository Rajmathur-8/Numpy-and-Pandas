import pandas as pd

"""
Data Cleaning : the process of identifying and 
                correcting (or removing) errors 
                and inconsistencies 
                ~75% of work done with Pandas
                is Data Cleaning
"""

df = pd.read_csv('pokemon.csv')

df = df.drop(columns=['Generation', 'Legendary','#'])  # drop unnecessary columns
print("After Dropping Columns:\n", df.to_string())

# handle missing values
df = df.dropna(subset=['Type 2'])  # drop rows with any missing values
print("After Dropping Missing Values:\n", df.to_string())

df = df.fillna({'Type 2': 'None'})  # fill missing values with a specific value
print("After Filling Missing Values:\n", df.to_string())

# fix inconsistent data
df['Type 1'] = df['Type 1'].str.capitalize()  # standardize text data
df['Legendary'] = df['Legendary'].astype(bool)  # convert to boolean
print("After Standardizing Text Data:\n", df.to_string())

# remove duplicates
df = df.drop_duplicates()  # drop duplicate rows
print("After Dropping Duplicates:\n", df.to_string())