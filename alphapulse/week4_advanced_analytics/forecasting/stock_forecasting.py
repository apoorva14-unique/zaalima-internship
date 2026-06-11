import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    'alphapulse/week3_dashboard/data_preparation/final_dataset.csv'
)

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Rolling Average Forecast
df['Forecast'] = df['AAPL_Price'].rolling(30).mean()

# Plot
plt.figure(figsize=(14, 6))

plt.plot(
    df['Date'],
    df['AAPL_Price'],
    label='Actual Price'
)

plt.plot(
    df['Date'],
    df['Forecast'],
    label='30-Day Rolling Forecast'
)

plt.title('Apple Stock Trend Forecast')
plt.xlabel('Date')
plt.ylabel('Stock Price')
plt.legend()
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig(
    'alphapulse/week4_advanced_analytics/outputs/stock_forecast.png'
)

print("✅ Stock Forecasting Completed!")