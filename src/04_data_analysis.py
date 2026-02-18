import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('D:/Full projet/laptop-price-intelligence/data/laptops_final.csv')

#Interface settings
sns.set_theme(style="whitegrid") 
plt.rcParams['figure.figsize'] = (12, 6) 

df['Price'] = pd.to_numeric(df['Price'], errors='coerce')
df['RAM_GB'] = pd.to_numeric(df['RAM_GB'], errors='coerce')
df['SSD_GB'] = pd.to_numeric(df['SSD_GB'], errors='coerce')

print("The data is ready for graphing")

#Plot a histogram combined with a density curve (KDE)
plt.figure(figsize=(10, 6))
sns.histplot(data = df, x = 'Price', kde = True, color= 'skyblue',bins = 30)
plt.title('Laptop Price Distribution in the French Market', fontsize = 16)
plt.xlabel('Price (euro)', fontsize = 12)
plt.ylabel('Number of laptop', fontsize = 12)
plt.show()