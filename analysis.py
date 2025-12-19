import pandas as pd
import numpy as np

athletes = pd.read_csv('athlete_events.csv')
regions = pd.read_csv('noc_regions.csv')

df = pd.merge(athletes, regions, on='NOC', how='left')

print("Data Loaded! Here are the first 5 rows:")
print(df.head())


df['Medal'] = df['Medal'].fillna('None')


df['Age'] = df['Age'].fillna(df['Age'].median())
df['Height'] = df['Height'].fillna(df['Height'].median())

print(f"Missing values handled! Total rows: {len(df)}")

host_map = {
    'Sydney': 'Australia', 'Athens': 'Greece', 'Beijing': 'China', 
    'London': 'UK', 'Rio de Janeiro': 'Brazil', 'Tokyo': 'Japan',
    'Atlanta': 'USA', 'Barcelona': 'Spain', 'Seoul': 'South Korea'
}

df['Is_Host'] = np.where(df['City'].map(host_map) == df['region'], 1, 0)

host_comparison = df[df['Medal'] != 'None'].groupby(['region', 'Is_Host'])['Medal'].count().unstack()
print(host_comparison.loc[['USA', 'China', 'UK']].dropna())

import matplotlib.pyplot as plt
top_10_countries = df[df['Medal'] != 'None']['region'].value_counts().head(10)

plt.figure(figsize=(12, 6))
top_10_countries.plot(kind='bar', color='skyblue', edgecolor='black')
plt.title('Top 10 Countries with Most Olympic Medals (1896-2016)', fontsize=15)
plt.xlabel('Country', fontsize=12)
plt.ylabel('Number of Medals', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout() 
plt.savefig('top_countries_chart.png') 
plt.show() 