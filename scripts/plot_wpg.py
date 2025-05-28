import pandas as pd

# Load the uploaded CSV file
df_spain = pd.read_csv('../data/cases_deaths_spain.csv')

import matplotlib.pyplot as plt

df_spain['date'] = pd.to_datetime(df_spain['date'])
df_spain['weekly_pct_growth_cases'] = df_spain['weekly_pct_growth_cases'].fillna(0)

# Plot for weekly percentage growth
plt.figure(figsize=(14, 6))
plt.plot(df_spain['date'], df_spain['weekly_pct_growth_cases'], color='purple', label='Weekly % Growth in Cases')

plt.title('Weekly Percentage Growth in COVID-19 Cases in Spain')
plt.xlabel('Date')
plt.ylabel('Weekly Growth (%)')
plt.axhline(0, color='black', linestyle='--', linewidth=1)
plt.legend()
plt.tight_layout()
plt.savefig('../images/wpg.png', format="png", bbox_inches="tight")
plt.show()
