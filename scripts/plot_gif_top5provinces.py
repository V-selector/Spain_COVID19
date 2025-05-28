import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

# Load dataset
df_provinces = pd.read_csv('../data/cases_per_province.csv')
df_provinces['fecha'] = pd.to_datetime(df_provinces['fecha'])

# Filter for years 2020 and 2021
df_filtered = df_provinces[df_provinces['fecha'].dt.year.isin([2020, 2021])]

# Compute total cases per province and get top 5
total_cases_by_prov = df_filtered.groupby('provincia_iso')['num_casos'].sum().sort_values(ascending=False)
top5_provinces = total_cases_by_prov.head(5).index.tolist()

# Filter original dataframe to include only the top 5 provinces
df_top5 = df_filtered[df_filtered['provincia_iso'].isin(top5_provinces)]

# Group by date and province, then sum cases
df_grouped = df_top5.groupby(['fecha', 'provincia_iso'])['num_casos'].sum().reset_index()

# Pivot table to prepare for plotting
df_plot = df_grouped.pivot(index='fecha', columns='provincia_iso', values='num_casos').fillna(0)
dates = df_plot.index
provinces = df_plot.columns

# Province code to name mapping
province_name = {
    'A': 'Alicante', 'AB': 'Albacete', 'AL': 'Almería', 'AV': 'Ávila', 'B': 'Barcelona',
    'BA': 'Badajoz', 'BI': 'Bizkaia', 'BU': 'Burgos', 'C': 'A Coruña', 'CA': 'Cádiz',
    'CC': 'Cáceres', 'CE': 'Ceuta', 'CO': 'Córdoba', 'CR': 'Ciudad Real', 'CS': 'Castellón',
    'CU': 'Cuenca', 'GC': 'Las Palmas', 'GI': 'Girona', 'GR': 'Granada', 'GU': 'Guadalajara',
    'H': 'Huelva', 'HU': 'Huesca', 'J': 'Jaén', 'L': 'Lleida', 'LE': 'León', 'LO': 'La Rioja',
    'LU': 'Lugo', 'M': 'Madrid', 'MA': 'Málaga', 'ML': 'Melilla', 'MU': 'Murcia',
    'NC': 'Navarra', 'O': 'Asturias', 'OR': 'Ourense', 'P': 'Palencia', 'PM': 'Baleares',
    'PO': 'Pontevedra', 'S': 'Cantabria', 'SA': 'Salamanca', 'SE': 'Sevilla', 'SG': 'Segovia',
    'SO': 'Soria', 'SS': 'Gipuzkoa', 'T': 'Tarragona', 'TE': 'Teruel', 'TF': 'Santa Cruz de Tenerife',
    'TO': 'Toledo', 'V': 'Valencia', 'VA': 'Valladolid', 'VI': 'Álava', 'ZA': 'Zamora', 'Z': 'Zaragoza'
}

# Create the figure and axes
fig, ax = plt.subplots(figsize=(14, 7))
lines = {prov: ax.plot([], [], label=province_name.get(prov, prov))[0] for prov in provinces}
ax.set_xlim(dates.min(), dates.max())
ax.set_ylim(0, df_plot.values.max() * 1.1)
ax.set_title("Daily COVID-19 Cases in 2020–2021 (Top 5 Provinces)")
ax.set_xlabel("Date")
ax.set_ylabel("Number of Cases")
ax.legend(title="Province")

# Animation update function
def update(frame):
    current_date = dates[:frame]
    for prov in provinces:
        lines[prov].set_data(current_date, df_plot[prov].iloc[:frame])
    return lines.values()

# Create animation
anim = FuncAnimation(fig, update, frames=len(dates), interval=30, blit=True)

# Save to GIF
anim.save('../images/top5provinces.gif', writer=PillowWriter(fps=20))
