import pandas as pd

df = pd.read_csv('pokemon.csv', index_col='Name')

# print("Original DataFrame:\n", df.to_string())

#print(df.mean(numeric_only=True))  # Mean of all numeric columns
#print(df.sum(numeric_only=True))   # Sum of all numeric columns
# print("Min\n",df.min(numeric_only=True))   # Minimum of all numeric columns
# print("Max\n",df.max(numeric_only=True))   # Maximum of all numeric columns

# print("Count\n",df.count())   # Count of non-NA/null entries for each column
# print("Median\n",df.median(numeric_only=True))   # Median of all
# print("Std Dev\n",df.std(numeric_only=True))   # Standard deviation of all numeric columns
# print("Variance\n",df.var(numeric_only=True))   # Variance of all


# Single column aggregation
print(df['Speed'].mean(numeric_only=True))
print(df['HP'].sum(numeric_only=True))
print(df['Attack'].max(numeric_only=True))
print(df['Defense'].min(numeric_only=True))

# group by
group1 = df.groupby('Type 1')
print(group1["Attack"].mean(numeric_only=True))
print(group1["Attack"].min(numeric_only=True))
print(group1["Attack"].max(numeric_only=True))