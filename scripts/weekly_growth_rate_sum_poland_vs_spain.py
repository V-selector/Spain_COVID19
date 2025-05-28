import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('../data/cases_deaths_worldwide.csv',
    parse_dates=['date']
)
df = df[df['country'].isin(['Poland', 'Spain'])]
df['year'] = df['date'].dt.year

growth = (
    df.groupby(['country','year'])['weekly_pct_growth_cases']
      .sum()
      .reset_index()
)
growth = growth[growth['year'].between(2020, 2023)]

years = sorted(growth['year'].unique())
x = np.arange(len(years))
width = 0.35

fig, ax = plt.subplots(figsize=(10,6))
bars_poland = ax.bar(
    x - width/2,
    growth[growth['country']=='Poland']['weekly_pct_growth_cases'],
    width, label='Poland'
)
bars_spain = ax.bar(
    x + width/2,
    growth[growth['country']=='Spain']['weekly_pct_growth_cases'],
    width, label='Spain'
)

for bar in list(bars_poland) + list(bars_spain):
    height = bar.get_height()
    xpos = bar.get_x() + bar.get_width()/2

    ax.annotate(
        f"{int(height):,}",      
        xy=(xpos, height),       
        xytext=(0, 2 if height>=0 else -3),  
        textcoords='offset points',
        ha='center',
        va='bottom' if height>=0 else 'top',
        fontsize=10
    )

ax.set_xticks(x)
ax.set_xticklabels(years)
ax.set_xlabel('Year',fontsize=14, fontweight='bold')
ax.set_ylabel('Sum of Weekly Growth Rates (%)',fontsize=14, fontweight='bold')
ax.set_title('Poland vs Spain: Annual Cumulative Weekly Growth Rate\n(2020–2023)',fontsize=16, fontweight='bold')
ax.legend(loc='upper right')
ax.grid(axis='y', linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig("../images/weekly_growth_rate_sum_poland_vs_spain(2020-2023).png")
plt.show()