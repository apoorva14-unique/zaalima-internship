import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('alphapulse/week3_dashboard/data_preparation/final_dataset.csv')

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Moving Averages
df['AAPL_20_Day_MA'] = df['AAPL_Price'].rolling(window=20).mean()
df['AAPL_50_Day_MA'] = df['AAPL_Price'].rolling(window=50).mean()

# Plot
plt.figure(figsize=(14,6))

plt.plot(df['Date'], df['AAPL_Price'], label='Apple Stock Price')
plt.plot(df['Date'], df['AAPL_20_Day_MA'], label='20-Day Moving Average')
plt.plot(df['Date'], df['AAPL_50_Day_MA'], label='50-Day Moving Average')

plt.title('Apple Stock Moving Average Strategy')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()

# Save output
plt.savefig('alphapulse/week4_advanced_analytics/outputs/moving_average_strategy.png')

print("✅ Moving Average Strategy Completed!")