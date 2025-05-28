import pandas as pd
import plotly.graph_objects as go
 

df = pd.read_csv('../data/vaccinations_age_worldwide.csv',
    parse_dates=['date']
)
df['year'] = df['date'].dt.year
df = df[df['country'].isin(['Poland', 'Spain'])]

overall = (
    df
    .groupby(['country','year'])['people_vaccinated_per_hundred']
    .mean()
    .reset_index()
)

fig = go.Figure()
colors = {'Poland':'#1f77b4', 'Spain':'#ff7f0e'}

for country in ['Poland','Spain']:
    subset = overall[overall['country']==country]
    fig.add_trace(go.Scatter(
        x=subset['year'],
        y=subset['people_vaccinated_per_hundred'],
        mode='lines+markers',
        name=country,
        line=dict(color=colors[country], width=2),
        marker=dict(size=8)
    ))

fig.update_layout(
    title=dict(
        text='Poland vs Spain: Annual Vaccination Rate (Interactive)',
        x=0.5,
        font=dict(size=24, family='Arial', color='#333')
    ),
    xaxis=dict(
        title=dict(text='Year', font=dict(size=18)),
        tickfont=dict(size=14),
        dtick=1
    ),
    yaxis=dict(
        title=dict(text='Vaccination Rate (%)', font=dict(size=18)),
        tickfont=dict(size=14)
    ),
    legend=dict(
        title=dict(text='Country', font=dict(size=16)),
        font=dict(size=14),
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5
    ),
    font=dict(  
        family='Arial',
        size=14,
        color='#333'
    ),
    margin=dict(l=50, r=50, t=80, b=50),
    width=900, height=600
)

html_path = '../images/overall_vaccination_rate_poland_vs_spain.html'
fig.write_html(
    html_path,
    include_plotlyjs="cdn",  
    full_html=True,           
    auto_open=True            
)

print(f"Interactive chart saved and opened in browser: {html_path}")