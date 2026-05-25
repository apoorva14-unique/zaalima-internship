import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load returns data
returns = pd.read_csv(
    'alphapulse/data/processed/daily_returns.csv'
)

# Remove Date column
returns = returns.drop(columns=['Date'])

# Correlation matrix
corr = returns.corr()

print(corr)

# Plot heatmap
plt.figure(figsize=(12, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap='coolwarm'
)

plt.title('Stock Correlation Heatmap')

# Save image
plt.savefig(
    'alphapulse/data/processed/correlation_heatmap.png'
)

# plt.show()

# Save image
plt.savefig(
    'alphapulse/data/processed/correlation_heatmap.png'
)

print("✅ Correlation Heatmap Created!")