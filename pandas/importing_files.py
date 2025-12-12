import pandas as pd

# importing csv file
df = pd.read_csv('data_csv.csv')
print("CSV Data:\n", df)

# to print All sheet names
#print(df.to_string())

# 1st 5 rows
print("First 5 rows:\n", df.head())
# last 5 rows
print("Last 5 rows:\n", df.tail())

# importing json file
df_json = pd.read_json('data_json.json')
print("JSON Data:\n", df_json)

