import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load & join data
cases = pd.read_csv('../data/cases_deaths_spain.csv', parse_dates=['date']).set_index('date')
hosp  = pd.read_csv('../data/hospital_spain.csv',       parse_dates=['date']).set_index('date')
df = cases[['new_cases','new_deaths']].join(
    hosp[['daily_occupancy_hosp','daily_occupancy_icu']],
    how='inner'
)

# Compute correlation
corr = df.corr()

# Plot
plt.figure(figsize=(6, 5))
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of COVID Metrics in Spain')
plt.tight_layout()

# Save and close
out = '../images/spain_correlation_matrix.png'
plt.savefig(out)
print(f"Saved {out}")
plt.close()
