import pandas as pd

# Load the uploaded CSV file
df_spain = pd.read_csv('../data/cases_deaths_spain.csv')

import matplotlib.pyplot as plt

df_spain['cfr_100_cases'] = df_spain['cfr_100_cases'].fillna(0)
df_spain['date'] = pd.to_datetime(df_spain['date'])

# Case fatality rate plot
plt.figure(figsize=(14, 6))
plt.plot(df_spain['date'], df_spain['cfr_100_cases'], color='red', label='CFR (per 100 cases)')

plt.title('Case Fatality Rate (CFR) per 100 Cases in Spain')
plt.xlabel('Date')
plt.ylabel('Deaths per 100 Cases')
plt.legend()
plt.tight_layout()
plt.savefig('../images/cfr.png', format="png", bbox_inches="tight")
plt.show()
