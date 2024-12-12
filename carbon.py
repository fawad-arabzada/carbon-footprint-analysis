import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

file_path = r"C:\Users\User\Desktop\Carbon Project\dataset.csv"
data = pd.read_csv(file_path, delimiter=',', encoding='utf-8')  

print(data.columns)  

data.columns = data.columns.str.strip()

print(data.columns)

print(data.head())  

print(data.isnull().sum()) 

print(data.duplicated().sum()) 

# Data Visualization
if 'sector' in data.columns:  
    sector_emissions = data.groupby('sector')['value'].sum()  # Summing emissions per sector
    sector_emissions.plot(kind='bar', color='skyblue', figsize=(10, 6))

    plt.title('Total CO2 Emissions by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Emissions (tons)')
    plt.xticks(rotation=45)  
    plt.show()
else:
    print("'sector' column not found in the dataset.")


data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')  

plt.figure(figsize=(10, 6))
plt.scatter(data['timestamp'], data['value'], color='purple', alpha=0.5)
plt.title('CO2 Emissions Over Time')
plt.xlabel('Date')
plt.ylabel('Emissions (tons)')
plt.xticks(rotation=45)
plt.show()

country_emissions = data.groupby(['country', 'timestamp'])['value'].sum().unstack()
country_emissions.plot(kind='line', figsize=(10, 6))

plt.title('CO2 Emissions Over Time by Country')
plt.xlabel('Date')
plt.ylabel('Emissions (tons)')
plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend position
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(data['value'], bins=30, color='teal', edgecolor='black')
plt.title('Distribution of CO2 Emissions')
plt.xlabel('Emissions (tons)')
plt.ylabel('Frequency')
plt.show()

plt.figure(figsize=(10, 6))
sns.boxplot(x='sector', y='value', data=data, palette='Set2')
plt.title('Emissions by Sector')
plt.xlabel('Sector')
plt.ylabel('Emissions (tons)')
plt.xticks(rotation=45)
plt.show()


