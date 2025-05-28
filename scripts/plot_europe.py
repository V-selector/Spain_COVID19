import pandas as pd 
import matplotlib.pyplot as plt


df_cleaned = pd.read_csv('../data/cases_deaths_worldwide_cleaned.csv')
# List of the 7 European countries with the highest total COVID-19 case counts
top_european_countries = [
    'France', 
    'Germany', 
    'United Kingdom',  
    'Italy', 
    'Spain', 
    'Netherlands', 
    'Poland' 
]

# Filter the cleaned DataFrame to include only these countries
europe_df = df_cleaned[df_cleaned['country'].isin(top_european_countries)]
# Convert 'date' column to datetime format

europe_df['date'] = pd.to_datetime(europe_df['date'])
# Create the plot
plt.figure(figsize=(14, 8))  # Set the figure size
for country in top_european_countries:
    country_data = europe_df[europe_df['country'] == country]  # Get data for each country
    plt.plot(country_data['date'], country_data['total_cases'], label=country)  # Plot total cases over time

# Add plot title and labels
plt.title('Top European Countries in Total COVID-19 Cases', fontsize=16)
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.legend()
plt.tight_layout()

plt.savefig('../images/europe.png', format='png', bbox_inches='tight')

plt.show()
