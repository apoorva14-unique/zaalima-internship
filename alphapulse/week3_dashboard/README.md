# AlphaPulse – Financial Market Analytics Dashboard

## Overview

AlphaPulse is a financial analytics project developed to analyze historical stock market data and provide interactive investment insights using Python and Power BI.

The dashboard enables users to explore stock performance, sector-wise analysis, volatility, cumulative returns, moving averages, and overall market trends through interactive visualizations and filters.

---

## Objectives

- Analyze historical stock market performance
- Compare daily returns and investment growth
- Evaluate stock volatility and market risk
- Monitor sector-wise performance
- Build an interactive dashboard for financial decision-making

---

## Dashboard Features

### Interactive Filters

- Stock (Ticker) Filter
- Sector Filter
- Trend Signal Filter (Bullish/Bearish)
- Date Range Slicer

---

### KPI Cards

- Average Portfolio Return (%)
- Average Daily Return
- Maximum Volatility
- Investment Growth Index
- Stocks Tracked

---

### Visualizations

- Stock Price Trend Over Time
- Sector Performance (Average Return %)
- 5-Year Cumulative Return by Stock
- Moving Average Analysis (Price, MA20, MA50)
- Risk vs Return Analysis
- 20-Day Volatility Trend

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Power BI
- Git
- GitHub
- VS Code
- yFinance

---

## Dataset

The dashboard uses historical stock market data collected through the **yFinance** library.

### Stocks Included

- Apple (AAPL)
- Microsoft (MSFT)
- NVIDIA (NVDA)
- Tesla (TSLA)
- JPMorgan Chase (JPM)
- Bank of America (BAC)
- Pfizer (PFE)
- Exxon Mobil (XOM)
- Walmart (WMT)
- Verizon (VZ)
- S&P 500 (^GSPC)

---

## Dashboard Insights

- Compare performance across multiple stocks and sectors
- Identify bullish and bearish market trends
- Analyze price movement using 20-day and 50-day moving averages
- Evaluate stock volatility over time
- Compare risk versus return for investment decisions
- Track cumulative investment growth over five years

---

## Dashboard Preview

![Dashboard](visuals/alphapulse_dashboard.png)

---

## Project Structure

```text
week3_dashboard/
│
├── data_preparation/
│   ├── final_dataset.py
│   ├── final_dataset.csv
│   └── final_dataset_long.csv
│
├── reports/
│   └── AlphaPulse_Dashboard.pbix
│
├── visuals/
│   └── alphapulse_dashboard.png
│
└── README.md
```

---

## Learning Outcomes

Through this project, I gained hands-on experience in:

- Financial data analysis
- Data preprocessing using Python
- Time-series analysis
- Moving average calculations
- Volatility analysis
- Portfolio performance analysis
- Interactive dashboard development
- Power BI data modeling
- KPI design and reporting
- Data storytelling and visualization

---

## Future Improvements

- Real-time stock market data integration
- Machine Learning-based price forecasting
- Sharpe Ratio and CAPM analysis
- Portfolio optimization recommendations
- Advanced financial KPIs
- Drill-through reports and custom tooltips

---