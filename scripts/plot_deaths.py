import pandas as pd

# Load the uploaded CSV file
df_spain = pd.read_csv('../data/cases_deaths_spain.csv')

import matplotlib.pyplot as plt

# Convert the 'date' column to datetime format
df_spain['date'] = pd.to_datetime(df_spain['date'])

# Plotting a timeline with bars for new cases and new deaths
plt.figure(figsize=(14, 6))
plt.bar(df_spain['date'], df_spain['new_deaths'], width=2.5, label='New Deaths' ,color='blue')


plt.title('Daily COVID-19 Deaths in Spain')
plt.xlabel('Date')
plt.ylabel('Deaths')
plt.legend()
plt.tight_layout()
plt.savefig('../images/deaths.png', format="png", bbox_inches="tight")
plt.show()
