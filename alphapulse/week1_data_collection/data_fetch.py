# AlphaPulse - Stock Data Collection
# Week 1 Data Collection

import yfinance as yf
import pandas as pd
import time

# Stock symbols
stocks = [
    "AAPL",
    "MSFT",
    "NVDA",
    "TSLA",
    "JPM",
    "BAC",
    "PFE",
    "XOM",
    "WMT",
    "VZ",
    "^GSPC"
]

# Empty dataframe
all_data = pd.DataFrame()

print("Downloading stock market data...\n")

# Download stock data one by one
for stock in stocks:

    try:

        print(f"Downloading {stock}...")

        data = yf.download(
            stock,
            start="2020-01-01",
            end="2025-01-01",
            auto_adjust=True,
            progress=False
        )

        # Store closing prices
        all_data[stock] = data['Close']

        # Delay to avoid API issues
        time.sleep(2)

    except Exception as e:

        print(f"Failed to download {stock}: {e}")

# Add Date column
all_data.reset_index(inplace=True)

# Preview dataset
print("\nDataset Preview:")
print(all_data.head())

# Save dataset
all_data.to_csv(
    "alphapulse/data/raw/stock_prices.csv",
    index=False
)

print("\n✅ Stock market dataset downloaded successfully!")