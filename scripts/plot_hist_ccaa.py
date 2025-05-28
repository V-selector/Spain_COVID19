import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df_ccaa = pd.read_csv('../data/cases_per_ccaa.csv')

# Aggregate total cases by CCAA
total_cases_ccaa = df_ccaa.groupby('ccaa_iso')['num_casos'].sum().reset_index()

# Mapping CCAA ISO codes to full names
ccaa_name_map = {
    'AN': 'Andalusia', 'AR': 'Aragon', 'AS': 'Asturias', 'CB': 'Cantabria',
    'CE': 'Ceuta', 'CL': 'Castile and León', 'CM': 'Castilla-La Mancha',
    'CN': 'Canary Islands', 'CT': 'Catalonia', 'EX': 'Extremadura',
    'GA': 'Galicia', 'IB': 'Balearic Islands', 'MC': 'Murcia', 'MD': 'Madrid',
    'ML': 'Melilla', 'NC': 'Navarre', 'PV': 'Basque Country', 'RI': 'La Rioja',
    'VC': 'Valencian Community'
}

# Map full names
total_cases_ccaa['ccaa_name'] = total_cases_ccaa['ccaa_iso'].map(ccaa_name_map)

# Plot histogram
plt.figure(figsize=(12, 6))
plt.barh(total_cases_ccaa['ccaa_name'], total_cases_ccaa['num_casos'], color='steelblue')
plt.xlabel('Total COVID-19 Cases')
plt.title('Total COVID-19 Cases by Autonomous Community in 2020-2021')
plt.tight_layout()
plt.savefig('../images/hist_ccaa.png', format='png', bbox_inches='tight')

plt.show()
