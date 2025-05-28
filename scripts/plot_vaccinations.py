import pandas as pd

# Load the vaccination dataset
df_vacc = pd.read_csv('../data/vaccinations_age_spain.csv')

import matplotlib.pyplot as plt

# Convert date to datetime
df_vacc['date'] = pd.to_datetime(df_vacc['date'])
plt.figure(figsize=(14, 8))

# Plot a line for each age group
for age_group in sorted(df_vacc['age_group'].unique()):
    group_data = df_vacc[df_vacc['age_group'] == age_group]
    plt.plot(group_data['date'], group_data['people_fully_vaccinated_per_hundred'],
             label=age_group)

# Formatting
plt.title('Fully Vaccinated People Over Time by Age Group in Spain')
plt.xlabel('Date')
plt.ylabel('Fully Vaccinated per 100 People')
plt.legend(title='Age Group', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig('../images/vaccinations.png', format='png', bbox_inches='tight')

plt.show()
