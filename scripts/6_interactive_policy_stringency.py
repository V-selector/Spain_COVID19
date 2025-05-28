import pandas as pd
import plotly.express as px


# Load data
df = pd.read_csv('../data/oxcgrt_policy_spain.csv', parse_dates=['date'])

fig = px.line(
    df,
    x='date',
    y='stringency_index',
    title='Stringency Index of COVID Policies in Spain'
)
fig.update_traces(mode='markers+lines')

out = '../images/interactive_policy_stringency.html'
fig.write_html(out)
print(f"Saved {out}")
