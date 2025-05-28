import pandas as pd

# Load the dataset of COVID-19 cases in people over 60
df_60 = pd.read_csv('../data/cases_over_60.csv')

# Convert the 'fecha' column to datetime format
df_60['fecha'] = pd.to_datetime(df_60['fecha'])

# Aggregate total cases, hospitalizations, ICU admissions, and deaths per date
df_summary = df_60.groupby('fecha')[['num_casos', 'num_hosp', 'num_uci', 'num_def']].sum().reset_index()

import matplotlib.pyplot as plt

# Plotting all key metrics over time
plt.figure(figsize=(14, 7))
plt.plot(df_summary['fecha'], df_summary['num_casos'], label='Cases', color='orange')
plt.plot(df_summary['fecha'], df_summary['num_hosp'], label='Hospitalizations', color='blue')
plt.plot(df_summary['fecha'], df_summary['num_uci'], label='ICU Admissions', color='purple')
plt.plot(df_summary['fecha'], df_summary['num_def'], label='Deaths', color='red')

plt.title('COVID-19 Trends in People Aged 60+ in Spain')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig('../images/over_60.png', format='png', bbox_inches='tight')

plt.show()

                               
