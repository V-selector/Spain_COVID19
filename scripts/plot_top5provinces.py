import pandas as pd

# Redefine province code mapping dictionary
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


# Load the dataset
df_provinces = pd.read_csv('../data/cases_per_province.csv')

# Group by province and map cod_prov
df_prov = df_provinces.groupby('provincia_iso')['num_casos'].sum().reset_index()
df_prov['cod_prov'] = df_prov['provincia_iso'].map(provincia_iso_a_cod_prov)

province_name = {
    'A': 'Alicante', 'AB': 'Albacete', 'AL': 'Almería', 'AV': 'Ávila', 'B': 'Barcelona',
    'BA': 'Badajoz', 'BI': 'Bizkaia', 'BU': 'Burgos', 'C': 'A Coruña', 'CA': 'Cádiz',
    'CC': 'Cáceres', 'CE': 'Ceuta', 'CO': 'Córdoba', 'CR': 'Ciudad Real', 'CS': 'Castellón',
    'CU': 'Cuenca', 'GC': 'Las Palmas', 'GI': 'Girona', 'GR': 'Granada', 'GU': 'Guadalajara',
    'H': 'Huelva', 'HU': 'Huesca', 'J': 'Jaén', 'L': 'Lleida', 'LE': 'León', 'LO': 'La Rioja',
    'LU': 'Lugo', 'M': 'Madrid', 'MA': 'Málaga', 'ME': 'Melilla', 'MU': 'Murcia',
    'NC': 'Navarra', 'O': 'Asturias', 'OR': 'Ourense', 'P': 'Palencia', 'PM': 'Baleares',
    'PO': 'Pontevedra', 'S': 'Cantabria', 'SA': 'Salamanca', 'SE': 'Sevilla', 'SG': 'Segovia',
    'SO': 'Soria', 'SS': 'Gipuzkoa', 'T': 'Tarragona', 'TE': 'Teruel', 'TF': 'Santa Cruz de Tenerife',
    'TO': 'Toledo', 'V': 'Valencia', 'VA': 'Valladolid', 'VI': 'Álava', 'Z': 'Zaragoza', 'ZA': 'Zamora'
}

df_prov['province_name'] = df_prov['provincia_iso'].map(province_name)

# Convert 'fecha' to datetime format
df_provinces['fecha'] = pd.to_datetime(df_provinces['fecha'])

# Filter data for years 2020 and 2021
df_filtered = df_provinces[df_provinces['fecha'].dt.year.isin([2020, 2021])]

# Calculate total cases per province
total_cases_by_prov = df_filtered.groupby('provincia_iso')['num_casos'].sum().sort_values(ascending=False)

# Select top 5 provinces
top5_provinces = total_cases_by_prov.head(5).index.tolist()

# Filter original dataframe for those top 5 provinces
df_top5 = df_filtered[df_filtered['provincia_iso'].isin(top5_provinces)]

# Group by date and province, and sum cases
df_top5_grouped = df_top5.groupby(['fecha', 'provincia_iso'])['num_casos'].sum().reset_index()

# Pivot the data for plotting
df_plot = df_top5_grouped.pivot(index='fecha', columns='provincia_iso', values='num_casos').fillna(0)

# Plot
import matplotlib.pyplot as plt

plt.figure(figsize=(14, 7))
for col in df_plot.columns:
    plt.plot(df_plot.index, df_plot[col], label=province_name.get(col, col))

plt.title("Daily COVID-19 Cases in 2020–2021 (Top 5 Provinces)")
plt.xlabel("Date")
plt.ylabel("Number of Cases")
plt.legend(title='Province')
plt.tight_layout()
plt.savefig('../images/top5provinces.png', format='png', bbox_inches='tight')
plt.show()
