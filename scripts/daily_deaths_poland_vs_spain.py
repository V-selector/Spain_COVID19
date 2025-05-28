import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cases_deaths_worldwide.csv',
    parse_dates=['date']
)
df = df[df['country'].isin(['Poland', 'Spain'])]
df.sort_values('date', inplace=True)

df['deaths_7d_avg']  = (
    df.groupby('country')['new_deaths']
      .rolling(7, center=True)
      .mean()
      .reset_index(0, drop=True)
)

plt.figure(figsize=(8, 6))
for country, color in zip(['Poland', 'Spain'], ['tab:red', 'tab:green']):
    sub = df[df['country'] == country]
    plt.plot(
        sub['date'], sub['deaths_7d_avg'],
        label=country,
        color=color,
        linewidth=1  
    )

plt.title('Poland vs Spain: Daily New Deaths (7-day MA)', fontsize=16, fontweight='bold')
plt.xlabel('Date', fontsize=14, fontweight='bold')
plt.ylabel('New Deaths (7-day average)', fontsize=14, fontweight='bold')
plt.legend(loc='upper left', fontsize=12)
plt.grid(alpha=0.3)
plt.tight_layout()
plt.savefig("../images/daily_new_deaths_7day_MA_poland_vs_spain.png")
plt.show()