import pandas as pd
import numpy as np

# ----------------------------------------------------------------------
# 1. LOAD RAW DATA  (unchanged from your original script)
# ----------------------------------------------------------------------
prices = pd.read_csv('alphapulse/data/raw/stock_prices.csv')
returns = pd.read_csv('alphapulse/data/processed/daily_returns.csv')

prices['Date'] = pd.to_datetime(prices['Date'])
returns['Date'] = pd.to_datetime(returns['Date'])

# ----------------------------------------------------------------------
# 2. MERGE  (same logic as your original script)
# ----------------------------------------------------------------------
final_df = prices.merge(returns, on='Date', suffixes=('_Price', '_Return'))

# ----------------------------------------------------------------------
# 3. IDENTIFY TICKER COLUMNS
# ----------------------------------------------------------------------
# Pull out just the price columns to know which tickers exist in the data.
price_cols = [c for c in final_df.columns if c.endswith('_Price')]
tickers = [c.replace('_Price', '') for c in price_cols]

SECTOR_MAP = {
    'AAPL': 'Technology',
    'MSFT': 'Technology',
    'NVDA': 'Technology',
    'TSLA': 'Automotive/Tech',
    'JPM':  'Banking',
    'BAC':  'Banking',
    'PFE':  'Healthcare',
    'XOM':  'Energy',
    'WMT':  'Retail',
    'VZ':   'Telecom',
    '^GSPC': 'Market Index',
    'GSPC': 'Market Index',
}

# ----------------------------------------------------------------------
# 4. ADD ROLLING METRICS PER TICKER
# ----------------------------------------------------------------------
# These are the columns that turn a flat price table into something a
# dashboard can actually tell a story with: trend, volatility, and risk.
final_df = final_df.sort_values('Date').reset_index(drop=True)

for ticker in tickers:
    price_col = f'{ticker}_Price'
    return_col = f'{ticker}_Return'

    if price_col not in final_df.columns:
        continue

    # 20-day and 50-day moving averages -> powers a trend/momentum visual
    final_df[f'{ticker}_MA20'] = final_df[price_col].rolling(window=20).mean()
    final_df[f'{ticker}_MA50'] = final_df[price_col].rolling(window=50).mean()

    if return_col in final_df.columns:
        # 20-day rolling volatility (annualized) -> powers a real risk visual
        # instead of one static "Portfolio Risk Score" number
        final_df[f'{ticker}_Volatility20'] = (
            final_df[return_col].rolling(window=20).std() * np.sqrt(252) * 100
        )

        # Cumulative return from day 1 -> lets you show "growth of $100 invested"
        final_df[f'{ticker}_CumulativeReturn'] = (
            (1 + final_df[return_col]).cumprod() - 1
        ) * 100

# ----------------------------------------------------------------------
# 5. BUILD A LONG-FORMAT TABLE (this is the real fix for Power BI)
# ----------------------------------------------------------------------

records = []
for ticker in tickers:
    price_col = f'{ticker}_Price'
    return_col = f'{ticker}_Return'
    ma20_col = f'{ticker}_MA20'
    ma50_col = f'{ticker}_MA50'
    vol_col = f'{ticker}_Volatility20'
    cum_col = f'{ticker}_CumulativeReturn'

    if price_col not in final_df.columns:
        continue

    sub = pd.DataFrame({
        'Date': final_df['Date'],
        'Ticker': ticker,
        'Sector': SECTOR_MAP.get(ticker, 'Other'),
        'Price': final_df[price_col],
        'DailyReturn': final_df[return_col] if return_col in final_df.columns else np.nan,
        'MA20': final_df[ma20_col] if ma20_col in final_df.columns else np.nan,
        'MA50': final_df[ma50_col] if ma50_col in final_df.columns else np.nan,
        'Volatility20': final_df[vol_col] if vol_col in final_df.columns else np.nan,
        'CumulativeReturnPct': final_df[cum_col] if cum_col in final_df.columns else np.nan,
    })
    records.append(sub)

long_df = pd.concat(records, ignore_index=True)

long_df['TrendSignal'] = np.where(
    long_df['Price'] > long_df['MA20'], 'Above MA20 (Bullish)',
    np.where(long_df['Price'] < long_df['MA20'], 'Below MA20 (Bearish)', 'Neutral')
)

# ----------------------------------------------------------------------
# 6. SAVE OUTPUTS
# ----------------------------------------------------------------------
# Wide version: kept for backward compatibility with your existing visuals
final_df.to_csv('alphapulse/week3_dashboard/data_preparation/final_dataset.csv', index=False)

# Long version: THIS is the one you import into Power BI for the new dashboard
long_df.to_csv('alphapulse/week3_dashboard/data_preparation/final_dataset_long.csv', index=False)

print("Final wide dataset shape:", final_df.shape)
print("Final long dataset shape:", long_df.shape)
print("Tickers included:", tickers)
print("\n✅ Enhanced Dashboard Datasets Created!")
print("   -> final_dataset.csv       (wide format, same as before)")
print("   -> final_dataset_long.csv  (long format, NEW - use this in Power BI)")