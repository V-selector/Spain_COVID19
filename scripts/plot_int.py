import pandas as pd
import plotly.graph_objects as go


# Load the CSV file containing daily COVID-19 data for Spain
df_spain = pd.read_csv('../data/cases_deaths_spain.csv')


df_spain['date'] = pd.to_datetime(df_spain['date'])
df_spain['year'] = df_spain['date'].dt.year
df_by_year = df_spain.groupby(['year', 'date'])['new_cases'].sum().reset_index()

# Calculate the total number of new cases per year
yearly_totals = df_by_year.groupby('year')['new_cases'].sum().to_dict()


fig = go.Figure()

# List of unique years in the dataset
years = sorted(df_by_year['year'].unique())

# Create one bar chart trace per year
for i, year in enumerate(years):
    yearly_data = df_by_year[df_by_year['year'] == year]
    total_cases = yearly_totals[year]

    # Add the bar chart trace for this year
    fig.add_trace(go.Bar(
        x=yearly_data['date'],
        y=yearly_data['new_cases'],
        width=500_000_000,
        name=str(year),
        visible=(i == 0)  # Only show the first year by default
    ))

    # Add an annotation displaying the total cases for this year
    fig.add_annotation(
        text=f"Total cases in {year}: {total_cases:,}",
        xref="paper", yref="paper",
        x=0.5, y=1.05,
        showarrow=False,
        font=dict(size=16),
        visible=(i == 0)
    )

# Create dropdown buttons for each year to toggle visibility
buttons = []
for i, year in enumerate(years):
    visibility_mask = [False] * len(years)
    visibility_mask[i] = True

    buttons.append(dict(
        label=str(year),
        method="update",
        args=[
            {"visible": visibility_mask},
            {"annotations": [{
                "text": f"Total cases in {year}: {yearly_totals[year]:,}",
                "xref": "paper", "yref": "paper", "x": 0.5, "y": 1.05,
                "showarrow": False,
                "font": dict(size=16)
            }]}
        ]
    ))

# Add the dropdown menu to the layout
fig.update_layout(
    updatemenus=[dict(
        active=0,
        buttons=buttons,
        x=0.98,
        y=1.15,
        xanchor='right',
        yanchor='top'
    )],
    title="Daily COVID-19 Cases in Spain by Year",
    xaxis_title="Date",
    yaxis_title="New Cases per Day",
    height=600
)

# Save the interactive chart to an HTML file
file_path = "../images/cases_per_year_interactive.html"
fig.write_html(file_path)


