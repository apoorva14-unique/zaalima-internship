import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('alphapulse/week3_dashboard/data_preparation/final_dataset.csv')

# Select return columns
returns = df[['AAPL_Return', 'MSFT_Return', 'NVDA_Return', 'TSLA_Return']]

# Average returns
mean_returns = returns.mean()

# Risk calculation
risk = returns.std()

# Plot Risk vs Return
plt.figure(figsize=(10,6))

plt.scatter(risk, mean_returns)

# Add stock labels
for stock in returns.columns:
    plt.annotate(stock, (risk[stock], mean_returns[stock]))

plt.title('Portfolio Risk vs Return')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Expected Return')

# Save chart
plt.savefig('alphapulse/week4_advanced_analytics/outputs/portfolio_optimization.png')

print("✅ Portfolio Optimization Completed!")