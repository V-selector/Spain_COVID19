import os
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('../data/cases_deaths_worldwide.csv', parse_dates=['date'])

# Select top 10 by total cases
top10 = (
    df.groupby('country')['new_cases']
      .sum()
      .nlargest(10)
      .index
      .tolist()
)
df_top10 = df[df['country'].isin(top10)]

fig = px.line(
    df_top10,
    x='date',
    y='new_cases',
    color='country',
    title='Daily New Cases in Top 10 Countries by Total Cases'
)
fig.update_layout(hovermode='x unified')

out = '../images/interactive_top10_world_cases.html'
fig.write_html(out)
print(f"Saved {out}")
