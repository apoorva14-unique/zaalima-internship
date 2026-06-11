import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv(
    'alphapulse/week3_dashboard/data_preparation/final_dataset.csv'
)

# Select stock return columns
returns = df[
    ['AAPL_Return', 'MSFT_Return', 'NVDA_Return', 'TSLA_Return']
]

# Calculate average return
mean_returns = returns.mean()

# Calculate risk (standard deviation)
risk = returns.std()

# Create figure
plt.figure(figsize=(10, 6))

# Scatter plot
plt.scatter(risk, mean_returns, s=120)

# Add stock labels
for stock in returns.columns:
    plt.annotate(
        stock.replace('_Return', ''),
        (risk[stock], mean_returns[stock]),
        xytext=(5, 5),
        textcoords='offset points'
    )

# Chart formatting
plt.title('Portfolio Risk vs Return Analysis')
plt.xlabel('Risk (Standard Deviation)')
plt.ylabel('Average Daily Return')
plt.grid(True)
plt.tight_layout()

# Save chart
plt.savefig(
    'alphapulse/week4_advanced_analytics/outputs/portfolio_optimization.png'
)

print("✅ Portfolio Optimization Completed!")