import pandas as pd
import matplotlib.pyplot as plt

# Load and preprocess the data
df_hosp = pd.read_csv('../data/hospital_spain.csv')
df_hosp['date'] = pd.to_datetime(df_hosp['date'])

# Plot setup
plt.figure(figsize=(14, 7))

# Plot each metric
plt.plot(df_hosp['date'], df_hosp['daily_occupancy_hosp'], label='Daily Hospital Occupancy', color='orange')
plt.plot(df_hosp['date'], df_hosp['daily_occupancy_icu'], label='Daily ICU Occupancy', color='blue')
plt.plot(df_hosp['date'], df_hosp['weekly_admissions_hosp'], label='Weekly Hospital Admissions', color='green')
plt.plot(df_hosp['date'], df_hosp['weekly_admissions_icu'], label='Weekly ICU Admissions', color='red')

# Formatting
plt.title('COVID-19 Hospital Metrics in Spain')
plt.xlabel('Date')
plt.ylabel('Count')
plt.legend()
plt.tight_layout()
plt.savefig('../images/hospital_metrics.png', format='png', bbox_inches='tight')
plt.show()
