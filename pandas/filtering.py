import pandas as pd

df = pd.read_csv('pokemon.csv', index_col='#')

#print("Original DataFrame:\n", df.to_string())

# attack_greater_100 = df['Attack'] > 100
# filtered_df = df[attack_greater_100] 
# print(filtered_df.to_string())

# legendary_df = df[df['Legendary'] == 1]
# print(legendary_df.to_string())

# water_type_df = df[df['Type 1'] == 'Water']
# print(water_type_df.to_string())
# water_df = df[(df['Type 1'] == 'Water') | (df['Type 2'] == 'Water')]
# print(water_df.to_string())

high_attack_defense_df = df[(df['Attack'] > 100) & (df['Defense'] > 100)]
print(high_attack_defense_df.to_string())