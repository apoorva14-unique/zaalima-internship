# AlphaPulse - Data Cleaning
# Week 1 Data Cleaning

import pandas as pd

# Load dataset
df = pd.read_csv(
    "alphapulse/data/raw/stock_prices.csv"
)

# Preview dataset
print("Dataset Preview:\n")
print(df.head())

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values using forward fill
df = df.ffill()

# Dataset information
print("\nDataset Information:\n")
print(df.info())

# Save cleaned dataset
df.to_csv(
    "alphapulse/data/raw/cleaned_stock_data.csv",
    index=False
)

print("\n✅ Data cleaning completed successfully!")