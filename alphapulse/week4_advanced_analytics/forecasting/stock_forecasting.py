import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('alphapulse/week3_dashboard/data_preparation/final_dataset.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Simple Forecast using Rolling Mean
df['Forecast'] = df['AAPL_Price'].rolling(window=30).mean()

# Plot
plt.figure(figsize=(14,6))

plt.plot(df['Date'], df['AAPL_Price'], label='Actual Price')
plt.plot(df['Date'], df['Forecast'], label='Forecasted Trend')

plt.title('Apple Stock Forecast')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Save chart
plt.savefig('alphapulse/week4_advanced_analytics/outputs/stock_forecast.png')

print("✅ Stock Forecasting Completed!")