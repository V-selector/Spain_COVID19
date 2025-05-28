import pandas as pd
import plotly.graph_objects as go

# Load the new dataset containing cases per comunidad autónoma
df_ccaa = pd.read_csv('../data/cases_per_ccaa.csv')

# Convert the date column to datetime and extract year
df_ccaa['fecha'] = pd.to_datetime(df_ccaa['fecha'])
df_ccaa['year'] = df_ccaa['fecha'].dt.year

ccaa_name = {
    'AN': 'Andalucía',
    'AR': 'Aragón',
    'AS': 'Asturias',
    'IB': 'Baleares',
    'CN': 'Canarias',
    'CB': 'Cantabria',
    'CL': 'Castilla y León',
    'CM': 'Castilla-La Mancha',
    'CT': 'Cataluña',
    'VC': 'Comunidad Valenciana',
    'EX': 'Extremadura',
    'GA': 'Galicia',
    'MD': 'Madrid',
    'MC': 'Murcia',
    'NC': 'Navarra',
    'PV': 'País Vasco',
    'RI': 'La Rioja',
    'CE': 'Ceuta',
    'ML': 'Melilla'
}


# Group total cases per comunidad and year using the correct column name
df_summary_ccaa = df_ccaa.groupby(['ccaa_iso', 'year'])['num_casos'].sum().reset_index()
df_summary_ccaa['comunidad'] = df_summary_ccaa['ccaa_iso'].map(ccaa_name)

# Create interactive dropdown bar plot
fig = go.Figure()
years = sorted(df_summary_ccaa['year'].unique())

for i, year in enumerate(years):
    data = df_summary_ccaa[df_summary_ccaa['year'] == year]
    fig.add_trace(go.Bar(
        x=data['comunidad'],
        y=data['num_casos'],
        name=str(year),
        visible=(i == 0)
    ))

# Dropdown buttons
buttons = []
for i, year in enumerate(years):
    vis = [False] * len(years)
    vis[i] = True
    buttons.append(dict(
        label=str(year),
        method='update',
        args=[{'visible': vis},
              {'title': f'Total COVID-19 Cases by Comunidad Autónoma in {year}'}]
    ))

# Layout with dropdown menu
fig.update_layout(
    updatemenus=[dict(
        buttons=buttons,
        direction="down",
        showactive=True,
        x=0.98,
        xanchor="right",
        y=1.15,
        yanchor="top"
    )],
    title=f'Total COVID-19 Cases by Comunidad Autónoma in {years[0]}',
    xaxis_title="Comunidad Autónoma",
    yaxis_title="Total Cases",
    xaxis=dict(type='category'),
    height=600
)

# Save 
output_path = "../images/cases_per_ccaa_inter.html"
fig.write_html(output_path)





