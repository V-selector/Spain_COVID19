import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV file into a DataFrame
file_path = '../data/cases_per_ccaa.csv'
df = pd.read_csv(file_path)

# Create a mapping from ccaa_iso codes to full community names
ccaa_name_dict = {
    'AN': 'Andalucía',
    'AR': 'Aragón',
    'AS': 'Asturias',
    'CB': 'Cantabria',
    'CE': 'Ceuta',
    'CL': 'Castilla y León',
    'CM': 'Castilla-La Mancha',
    'CN': 'Canarias',
    'CT': 'Cataluña',
    'EX': 'Extremadura',
    'GA': 'Galicia',
    'IB': 'Islas Baleares',
    'MC': 'Murcia',
    'MD': 'Madrid',
    'ML': 'Melilla',
    'NC': 'Navarra',
    'PV': 'País Vasco',
    'RI': 'La Rioja',
    'VC': 'Comunidad Valenciana'
}


# Convert the 'fecha' column to datetime format
df['fecha'] = pd.to_datetime(df['fecha'])
df['ccaa_name'] = df['ccaa_iso'].map(ccaa_name_dict)

# Calculate the total number of cases per autonomous community and sort them from highest to lowest
total_cases_by_ccaa = df.groupby('ccaa_name')['num_casos'].sum().sort_values(ascending=False)
sorted_ccaa_list = total_cases_by_ccaa.index.tolist()

# Create a figure with a 7x3 grid of subplots
fig, axes = plt.subplots(7, 3, figsize=(18, 20), sharex=False)
axes = axes.flatten()  # Flatten the 2D array of axes into a 1D array for easy indexing

# Plot the daily case counts for each community
for i, ccaa in enumerate(sorted_ccaa_list):
    ccaa_data = df[df['ccaa_name'] == ccaa]  # Filter data for the specific community
    axes[i].plot(ccaa_data['fecha'], ccaa_data['num_casos'])  # Plot date vs daily cases
    axes[i].set_title(f"{ccaa}", fontsize=10)  # Set subplot title as the community code
    axes[i].set_ylabel("Number of cases")  # Y-axis label
    axes[i].set_xlabel("Date")  # X-axis label
    axes[i].xaxis.set_major_locator(mdates.MonthLocator(interval=4))  # Show date every 4 months
    axes[i].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))  # Format date as year-month
    axes[i].tick_params(axis='x', rotation=45)  # Rotate x-axis labels for readability

# Remove any extra empty subplots if total communities < 21
for j in range(len(sorted_ccaa_list), len(axes)):
    fig.delaxes(axes[j])

# Adjust layout and add a main title
fig.tight_layout()
plt.suptitle('Diary Cases in every CCAA', fontsize=16, y=1.02)
plt.savefig('../images/ccaa.png', format="png", bbox_inches="tight")
plt.show()

