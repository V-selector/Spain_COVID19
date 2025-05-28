import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import json
from shapely.geometry import shape

# Load CSV data
df_prov = pd.read_csv('../data/cases_per_province.csv')

# Group by province and sum cases
df_agg = df_prov.groupby('provincia_iso')['num_casos'].sum().reset_index()

# Map ISO codes to cod_prov (official province code used in GeoJSON)
provincia_iso_a_cod_prov = {
    'A': '03', 'AB': '02', 'AL': '04', 'AV': '05', 'B': '08', 'BA': '06', 'BI': '48',
    'BU': '09', 'C': '15', 'CA': '11', 'CC': '10', 'CE': '51', 'CO': '14', 'CR': '13',
    'CS': '12', 'CU': '16', 'GC': '35', 'GI': '17', 'GR': '18', 'GU': '19', 'H': '21',
    'HU': '22', 'J': '23', 'L': '25', 'LE': '24', 'LO': '26', 'LU': '27', 'M': '28',
    'MA': '29', 'ML': '52', 'MU': '30', 'NC': '31', 'O': '33', 'OR': '32', 'P': '34',
    'PM': '07', 'PO': '36', 'S': '39', 'SA': '37', 'SE': '41', 'SG': '40', 'SO': '42',
    'SS': '20', 'T': '43', 'TE': '44', 'TF': '38', 'TO': '45', 'V': '46', 'VA': '47',
    'VI': '01', 'ZA': '49', 'Z': '50'
}
df_agg['cod_prov'] = df_agg['provincia_iso'].map(provincia_iso_a_cod_prov)

# Load GeoJSON
with open('../data/spain-provinces.geojson', encoding='utf-8') as f:
    geojson_provincias = json.load(f)

# Convert GeoJSON features to GeoDataFrame safely
records = []
for feature in geojson_provincias["features"]:
    props = feature["properties"]
    props["geometry"] = shape(feature["geometry"])
    records.append(props)

gdf = gpd.GeoDataFrame(records, geometry="geometry")
gdf['cod_prov'] = gdf['cod_prov'].astype(str).str.zfill(2)

# Merge on cod_prov
gdf_merged = gdf.merge(df_agg, on='cod_prov')

# Plot map
fig, ax = plt.subplots(figsize=(10, 12))
gdf_merged.plot(
    column='num_casos',
    cmap='OrRd',
    linewidth=0.8,
    edgecolor='0.8',
    legend=True,
    ax=ax
)
ax.set_title("Total COVID-19 Cases by Spanish Province (2020–2021)", fontsize=15)
ax.axis('off')
plt.tight_layout()
plt.savefig('../images/static_map.png', format='png', bbox_inches='tight')
plt.show()

