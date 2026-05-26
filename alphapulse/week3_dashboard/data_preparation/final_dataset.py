import pandas as pd

# Load stock prices dataset
prices = pd.read_csv(
    'alphapulse/data/raw/stock_prices.csv'
)

# Load daily returns dataset
returns = pd.read_csv(
    'alphapulse/data/processed/daily_returns.csv'
)

# Merge datasets using Date column
final_df = prices.merge(
    returns,
    on='Date',
    suffixes=('_Price', '_Return')
)

# Preview data
print(final_df.head())

# Save final dataset
final_df.to_csv(
    'alphapulse/week3_dashboard/data_preparation/final_dataset.csv',
    index=False
)

print("✅ Final Dashboard Dataset Created!")