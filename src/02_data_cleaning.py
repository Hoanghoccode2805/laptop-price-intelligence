import pandas as pd
import numpy as np

df = pd.read_csv('D:/Full projet/laptop-price-intelligence/data/laptops_raw.csv')
print(f'Initial line count: {len(df)}')


# Duplicate handling
num_duplicated = df.duplicated(subset=['Name']).sum()
print(f'{num_duplicated} duplicate lines were found!')

if num_duplicated > 0:
    df = df.drop_duplicates(subset=['Name'], keep= 'first')
    print('Complete to delete the duplicate data')
else:
    print('The data is clean and free of duplicates')


# Handling price types
df['Price'] = df['Price'].str.replace(" ","").replace("\xa0","").replace("\u202f","")
df['Price'] = df['Price'].str.replace("€",".")
df['Price'] = df['Price'].astype(float)
print(df['Price'].dtypes) 
print(df['Price'].head())
print('\n')

# Handling missing data
print("--- Check missing value ---")
print(df.isna().sum())

df.dropna(subset= ['Price'], inplace= True)
df.reset_index(drop=True, inplace= True)
print("\n--- AFTER REMOVING THE MISSING PRICE LINE ---")
print(f'Number of machines remaining after filtering: {len(df)}')


# Save data
df.to_csv('D:/Full projet/laptop-price-intelligence/data/laptops_processed.csv', index=False, encoding='utf-8-sig')
print("The file was saved at: laptops_processed.csv")