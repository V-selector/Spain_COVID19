import os
import pandas as pd
import plotly.express as px

# Create output folder
os.makedirs('plots', exist_ok=True)

# Load data
df = pd.read_csv('../data/vaccinations_age_spain.csv', parse_dates=['date'])
latest = df[df['date'] == df['date'].max()]

fig = px.bar(
    latest,
    x='age_group',
    y='people_vaccinated_per_hundred',
    labels={'people_vaccinated_per_hundred':'Vaccinated per 100','age_group':'Age Group'},
    title='People Vaccinated per 100 by Age Group in Spain (Latest)'
)

out = '../images/interactive_spain_vacc_age.html'
fig.write_html(out)
print(f"Saved {out}")
