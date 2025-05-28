# Requirements:
#   pip install pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt


# Load data
df = pd.read_csv('../data/vaccinations_age_spain.csv', parse_dates=['date'])
latest = df[df['date'] == df['date'].max()]

# Prepare arrays
age_groups = latest['age_group'].tolist()
vacc_per_100 = latest['people_vaccinated_per_hundred'].to_numpy()

# Plot
plt.figure(figsize=(10, 6))
plt.bar(age_groups, vacc_per_100)
plt.title('People Vaccinated per 100 by Age Group in Spain (Latest)')
plt.xlabel('Age Group')
plt.ylabel('Vaccinated per 100')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

# Save and close
out = '../images/spain_vacc_age.png'
plt.savefig(out)
print(f"Saved {out}")
plt.close()
