import pandas as pd

# Load the dataset with Spain's COVID-19 cases and deaths
df_spain = pd.read_csv('../data/cases_deaths_spain_monthly.csv')

# Convert 'date' column to datetime format
df_spain['date'] = pd.to_datetime(df_spain['year_month'])

# Filter data for years 2020 to 2022
df_spain_filtered = df_spain[df_spain['date'].dt.year.isin([2020, 2021, 2022])]

# Use montly new deaths as the time series
ts_cases = df_spain_filtered.set_index('date')['new_deaths'].fillna(0)

# Fit an AR model with 10 lags
from statsmodels.tsa.ar_model import AutoReg

ar_model = AutoReg(ts_cases, lags=10).fit()

# Predict next 250 days
forecast = ar_model.predict(start=len(ts_cases), end=len(ts_cases) + 23)
forecast_all = ar_model.predict(start=0, end=len(ts_cases) +23)

# Confidence interval (95%)
residuals_std = ar_model.resid.std()
ci_upper = forecast + 1.96 * residuals_std
ci_lower = forecast - 1.96 * residuals_std

# Prepare x-axis
import matplotlib.pyplot as plt
import pandas as pd

dates_past = ts_cases.index
dates_future = pd.date_range(start=dates_past[-1] + pd.DateOffset(months=1), periods=24, freq='MS')
all_dates = dates_past.append(dates_future)

# Plot
plt.figure(figsize=(14, 7))
plt.scatter(dates_past, ts_cases.values, label='Observed', color='black', s=10)
plt.plot(all_dates, forecast_all.values, label='Forecast (AR(10))', color='blue')
plt.fill_between(dates_future, ci_lower, ci_upper, color='skyblue', alpha=0.4, label='Uncertainty (95% CI)')

plt.title('Spain - AR(10) COVID-19 Death Forecast (Next Two Years) Using Data from 2020-2022')
plt.xlabel('Date')
plt.ylabel('Daily New Cases')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('../images/prediction_deaths.png', format='png', bbox_inches='tight')

plt.show()
