import pandas as pd
import plotly.graph_objects as go


policy = pd.read_csv('../data/oxcgrt_policy_worldwide.csv',
    parse_dates=['date']
)
policy['year'] = policy['date'].dt.year
policy = policy[policy['country'].isin(['Poland', 'Spain'])]

yearly = (
    policy
    .groupby(['country','year'])['stringency_index']
    .mean()
    .reset_index()
)

fig = go.Figure()
colors = {'Poland':'#6a0dad', 'Spain':'#008080'}

for country in ['Poland','Spain']:
    sub = yearly[yearly['country']==country]
    fig.add_trace(go.Scatter(
        x=sub['year'],
        y=sub['stringency_index'],
        mode='lines+markers',
        name=country,
        line=dict(color=colors[country], width=2),
        marker=dict(size=8)
    ))

fig.update_layout(
    title=dict(
        text='Poland vs Spain: Yearly Stringency Index',
        x=0.5,
        font=dict(size=24, family='Arial', color='#333')
    ),
    xaxis=dict(
        title=dict(text='Year', font=dict(size=18)),
        tickfont=dict(size=14),
        dtick=1
    ),
    yaxis=dict(
        title=dict(text='Stringency Index', font=dict(size=18)),
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

html_path = '../images/yearly_stringency_index_poland_vs_spain.html'
fig.write_html(
    html_path,
    include_plotlyjs='cdn',
    full_html=True,
    auto_open=True
)

print(f"Interactive chart saved and opened: {html_path}")
