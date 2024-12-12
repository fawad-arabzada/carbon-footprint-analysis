import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

file_path = r"C:\Users\User\Desktop\Carbon Project\dataset.csv"
try:
    data = pd.read_csv(file_path, delimiter=',', encoding='utf-8')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
    exit()

if 'timestamp' in data.columns:
    data['timestamp'] = pd.to_datetime(data['timestamp'], unit='s')
    data['year'] = data['timestamp'].dt.year
else:
    print("Error: 'timestamp' column not found in the dataset.")
    exit()

if 'value' not in data.columns:
    print("Error: 'value' column not found in the dataset.")
    exit()

aggregated_data = data.groupby('year')['value'].sum().reset_index()

fig_line = px.line(
    aggregated_data,
    x='year',
    y='value',
    title="CO2 Emissions Over Time (Aggregated by Year)",
    labels={"value": "Emissions (tons)", "year": "Year"},
)
fig_line.update_layout(width=800, height=400, template="plotly_dark")
fig_line.show()

if 'sector' in data.columns:
    sector_emissions = data.groupby('sector')['value'].sum()
    plt.figure(figsize=(10, 6))
    sector_emissions.plot(kind='bar', color='skyblue', edgecolor='black')
    plt.title('Total CO2 Emissions by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Emissions (tons)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("'sector' column not found in the dataset. Skipping sector-based bar chart.")

if 'sector' in data.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='sector', y='value', data=data, palette='Set2')
    plt.title('Emissions by Sector')
    plt.xlabel('Sector')
    plt.ylabel('Emissions (tons)')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
else:
    print("'sector' column not found in the dataset. Skipping sector-based boxplot.")

plt.figure(figsize=(10, 6))
plt.hist(data['value'], bins=30, color='teal', edgecolor='black')
plt.title('Distribution of CO2 Emissions')
plt.xlabel('Emissions (tons)')
plt.ylabel('Frequency')
plt.tight_layout()
plt.show()


print("\nSample of the Dataset:")
print(data.head())

if 'sector' in data.columns:
    print("\nAvailable Sectors:", data['sector'].unique())
