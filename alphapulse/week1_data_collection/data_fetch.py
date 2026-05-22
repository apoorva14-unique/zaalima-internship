import yfinance as yf
import pandas as pd
import time

# Stock List
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

all_data = pd.DataFrame()

print("Downloading stock market data...\n")

# Download one by one
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

        all_data[stock] = data['Close']

        time.sleep(2)

    except Exception as e:

        print(f"Failed for {stock}: {e}")

# Show Data
print("\nSample Data:")
print(all_data.head())

# Save CSV
all_data.to_csv(
    "alphapulse/data/raw/stock_prices.csv"
)

print("\n✅ Stock data downloaded successfully!")