import pandas as pd

# Load dataset
df = pd.read_csv('alphapulse/data/raw/stock_prices.csv')

print("Dataset Preview:")
print(df.head())

# Convert Date column
df['Date'] = pd.to_datetime(df['Date'])

# Set Date as index
df.set_index('Date', inplace=True)

# Calculate daily percentage returns
returns = df.pct_change()

# Remove NaN rows
returns = returns.dropna()

print("\nDaily Returns:")
print(returns.head())

# Save returns data
returns.to_csv(
    'alphapulse/data/processed/daily_returns.csv'
)

print("\n✅ Daily Returns Analysis Completed!")