import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df1 = pd.read_csv('../data/vaccinations_age_worldwide.csv', parse_dates=['date'])
df1['year'] = df1['date'].dt.year
df1 = df1[df1['country'].isin(['Poland', 'Spain'])]

by_age = (
    df1
    .groupby(['country','year','age_group'])['people_vaccinated_per_hundred']
    .mean()
    .reset_index()
)

avg_by_age = (
    by_age
    .groupby(['age_group','country'])['people_vaccinated_per_hundred']
    .mean()
    .unstack()   
)

age_groups = avg_by_age.index.tolist()
x = np.arange(len(age_groups))
width = 0.35

plt.figure(figsize=(8, 6))
plt.bar(x - width/2, avg_by_age['Poland'], width, label='Poland')
plt.bar(x + width/2, avg_by_age['Spain'],  width, label='Spain')

plt.xticks(x, age_groups, rotation=45, fontsize=12)
plt.xlabel('Age Group', fontsize=14, fontweight='bold')
plt.ylabel('Avg Vaccination Rate (%)', fontsize=14, fontweight='bold')
plt.title('Poland vs Spain: Average Vaccination Rate by Age Group', 
          fontsize=16, fontweight='bold')
plt.legend(loc='upper left', fontsize=12)
plt.tight_layout()
plt.savefig("../images/vaccination_by_age_group_poland_vs_spain.png")
plt.show()