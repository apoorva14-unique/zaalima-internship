import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load returns dataset
returns = pd.read_csv(
    'alphapulse/data/processed/daily_returns.csv'
)

# Remove Date column
returns = returns.drop(columns=['Date'])

# Select stock
stock = 'AAPL'

# Mean and standard deviation
mu = returns[stock].mean()
sigma = returns[stock].std()

# Simulation settings
days = 100
simulations = 50

# Initial stock price
start_price = 100

# Random seed
np.random.seed(42)

plt.figure(figsize=(12, 6))

# Run simulations
for i in range(simulations):

    prices = [start_price]

    for x in range(days):

        shock = np.random.normal(mu, sigma)

        next_price = prices[-1] * (1 + shock)

        prices.append(next_price)

    plt.plot(prices)

# Chart settings
plt.title(f'Monte Carlo Simulation - {stock}')
plt.xlabel('Days')
plt.ylabel('Simulated Price')

plt.tight_layout()

# Save plot
plt.savefig(
    'alphapulse/data/processed/monte_carlo_simulation.png'
)

# plt.show()

print("✅ Monte Carlo Simulation Completed!")