import pandas as pd
import numpy as np

# Load returns dataset
returns = pd.read_csv(
    'alphapulse/data/processed/daily_returns.csv'
)

# Remove Date column
returns = returns.drop(columns=['Date'])

print("\n95% Value at Risk (VaR)\n")

# Calculate VaR
for stock in returns.columns:

    var_95 = np.percentile(
        returns[stock].dropna(),
        5
    )

    print(f"{stock}: {var_95:.4f}")

print("\n✅ VaR Analysis Completed!")