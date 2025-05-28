# Requirements:
#   pip install pandas matplotlib imageio

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
import imageio

# Mapping ISO codes to full community names
ccaa_names = {
    'AN': 'Andalucía', 'AR': 'Aragón', 'AS': 'Asturias', 'CB': 'Cantabria',
    'CE': 'Ceuta', 'CL': 'Castilla y León', 'CM': 'Castilla-La Mancha',
    'CN': 'Canarias', 'CT': 'Cataluña', 'VC': 'Comunidad Valenciana',
    'EX': 'Extremadura', 'GA': 'Galicia', 'IB': 'Islas Baleares',
    'RI': 'La Rioja', 'MD': 'Comunidad de Madrid', 'ML': 'Melilla',
    'MU': 'Región de Murcia', 'NC': 'Navarra', 'PV': 'País Vasco'
}

# Load and preprocess data
df = pd.read_csv('../data/cases_per_ccaa.csv', parse_dates=['fecha'])
df = df.rename(columns={'fecha': 'date', 'ccaa_iso': 'region', 'num_casos': 'cases'})
df['region'] = df['region'].map(ccaa_names).fillna(df['region'])

# Daily pivot table: rows = dates, columns = regions
df_daily = (
    df.groupby(['date', 'region'])['cases']
      .sum()
      .unstack(fill_value=0)
      .sort_index()
)

# Compute cumulative cases
cumulative = df_daily.cumsum()

# Keep only days with data
cumulative = cumulative.loc[cumulative.sum(axis=1) > 0]

# Fix the bar order: sort regions by total cases on the last day
final_ranking = cumulative.iloc[-1].sort_values(ascending=False)
ordered_regions = final_ranking.index.tolist()
cumulative = cumulative[ordered_regions]  # fix column order

# Prepare colors
cmap = plt.get_cmap('tab20')
colors = {region: cmap(i % 20) for i, region in enumerate(ordered_regions)}

# Global max for consistent y-axis
global_max = cumulative.values.max() * 1.1

# Create frames for the GIF
frames = []

for dt, row in cumulative.iterrows():
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Always plot the same regions in the same order
    values = row[ordered_regions]
    bars = ax.bar(ordered_regions, values, color=[colors[r] for r in ordered_regions])
    
    ax.set_ylim(0, global_max)
    ax.set_title(f'Cumulative COVID-19 Cases by CCAA\n{dt:%Y-%m-%d}')
    ax.set_xlabel('Autonomous Community')
    ax.set_ylabel('Cumulative Cases')
    ax.yaxis.set_major_locator(MaxNLocator(nbins=5))
    plt.xticks(rotation=45, ha='right')

    # Annotate each bar
    for bar in bars:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width() / 2, h + global_max * 0.01,
                    f'{int(h)}', ha='center', va='bottom')

    plt.tight_layout()
    fig.canvas.draw()
    w, h = fig.canvas.get_width_height()
    img = np.frombuffer(fig.canvas.tostring_rgb(), dtype='uint8').reshape(h, w, 3)
    frames.append(img)
    plt.close(fig)

# Export the GIF 
imageio.mimsave('../images/cases_ccaa.gif', frames, duration=0.3)


