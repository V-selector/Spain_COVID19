import pandas as pd
import matplotlib.pyplot as plt


df_policy = pd.read_csv('../data/oxcgrt_policy_spain.csv')

# Convert the 'Date' column to datetime format
df_policy['date'] = pd.to_datetime(df_policy['date'])
# Select a few key policy indicators to plot
policy_columns = ['c1m_school_closing','c2m_workplace_closing', 'c3m_cancel_public_events', 'c4m_restrictions_on_gatherings', 'c5m_close_public_transport', 'c6m_stay_at_home_requirements', 'c7m_restrictions_on_internal_movement']

# Plotting the selected policies over time
plt.figure(figsize=(12, 6))
for col in policy_columns:
    plt.plot(df_policy['date'], df_policy[col], label=col)

plt.title('COVID-19 Policy Response in Spain', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Policy Stringency Level')
plt.legend()
plt.tight_layout()
plt.savefig('../images/restrictions.png', format='png', bbox_inches='tight')

plt.show()
