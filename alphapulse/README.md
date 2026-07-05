# AlphaPulse – Financial Market Analytics Project

## Overview

AlphaPulse is an end-to-end Financial Market Analytics project developed using **Python** and **Power BI** to analyze historical stock market data, evaluate financial risk, generate investment insights, and build interactive dashboards.

The project covers the complete analytics workflow—from data collection and preprocessing to quantitative analysis, dashboard development, forecasting, portfolio optimization, and workflow automation.

Developed as part of a **Financial Analytics & Data Analytics Internship**.

---

# Tech Stack

### Programming & Analytics
- Python
- Pandas
- NumPy
- Matplotlib

### Business Intelligence
- Power BI

### Development Tools
- VS Code
- Git
- GitHub

---

# Dataset

Historical stock market data collected using the **yfinance** library.

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

## Project Structure

```text
alphapulse/
│
├── README.md
│
├── data/
│   ├── raw/
│   │   ├── cleaned_stock_data.csv
│   │   └── stock_prices.csv
│   │
│   └── processed/
│       ├── daily_returns.csv
│       ├── correlation_heatmap.png
│       └── monte_carlo_simulation.png
│
├── reports/
│   ├── README.md
│   ├── alphapulse_dashboard.png
│   ├── correlation_heatmap.png
│   ├── daily_returns.csv
│   ├── monte_carlo_simulation.png
│   ├── moving_average_strategy.png
│   ├── portfolio_optimization.png
│   └── stock_forecast.png
│
├── week1_data_collection/
│   ├── data_fetch.py
│   ├── data_cleaning.py
│   └── cleaning_notes.md
│
├── week2_quantitative_analysis/
│   ├── returns_analysis.py
│   ├── correlation_heatmap.py
│   ├── monte_carlo.py
│   ├── var_analysis.py
│   └── README.md
│
├── week3_dashboard/
│   ├── data_preparation/
│   │   ├── final_dataset.py
│   │   ├── final_dataset.csv
│   │   └── final_dataset_long.csv
│   │
│   ├── powerbi/
│   │   └── alphapulse_dashboard.pbix
│   │
│   ├── visuals/
│   │   └── alphapulse_dashboard.png
│   │
│   └── README.md
│
└── week4_advanced_analytics/
    ├── forecasting/
    │   ├── moving_average_strategy.py
    │   └── stock_forecasting.py
    │
    ├── portfolio_analysis/
    │   └── portfolio_optimization.py
    │
    ├── automation/
    │   └── automated_pipeline.py
    │
    ├── outputs/
    │   ├── moving_average_strategy.png
    │   ├── portfolio_optimization.png
    │   └── stock_forecast.png
    │
    └── README.md
```

---

# Week 1 – Data Collection & Preparation

## Objectives

- Collect historical stock market data
- Clean and preprocess financial datasets
- Prepare data for analysis

### Tasks Performed

- Imported stock price data
- Cleaned missing values
- Standardized date formats
- Prepared structured datasets for analysis

### Outcome

A clean and reliable dataset ready for financial analytics.

---

# Week 2 – Quantitative Financial Analysis

## Objectives

- Analyze stock returns
- Evaluate investment risk
- Measure stock correlations
- Generate analytical insights

### Modules Developed

- Daily Returns Analysis
- Correlation Heatmap
- Value at Risk (VaR)
- Monte Carlo Simulation

### Outputs

- Daily Returns Dataset
- Correlation Heatmap
- Monte Carlo Simulation

### Key Insights

- Tesla showed the highest volatility.
- Apple and Microsoft demonstrated relatively stable growth.
- Banking stocks displayed positive correlation.
- The S&P 500 reflected long-term market trends.

---

# Week 3 – Interactive Financial Dashboard

## Objectives

Build a professional Power BI dashboard for analyzing stock performance, sector trends, investment growth, and market risk.

---

## Dashboard Features

### Interactive Filters

- Stock (Ticker)
- Sector
- Date Range
- Trend Signal

### KPI Cards

- Average Portfolio Return %
- Average Daily Return
- Maximum Volatility
- Investment Growth Index
- Stocks Tracked

### Visualizations

- Stock Price Trend Over Time
- Sector Performance (Average Return %)
- 5-Year Cumulative Return by Stock
- Moving Average Analysis (MA20 & MA50)
- Risk vs Return Analysis
- 20-Day Volatility Trend

---

## Dashboard Highlights

- Fully interactive dashboard
- Dynamic filtering using slicers
- Multi-stock comparison
- Sector-wise performance analysis
- Trend signal identification
- Professional financial dashboard layout

---

## Dashboard Preview

![AlphaPulse Dashboard](week3_dashboard/visuals/alphapulse_dashboard.png)

---

## Enhanced Dataset Engineering

To support interactive dashboard functionality, the dataset was enhanced by generating:

- Moving Average (20-Day)
- Moving Average (50-Day)
- 20-Day Rolling Volatility
- Cumulative Returns
- Trend Signal (Bullish/Bearish)
- Sector Classification

Two datasets were created:

- **final_dataset.csv** (Wide Format)
- **final_dataset_long.csv** (Long Format for Power BI)

---

# Week 4 – Advanced Financial Analytics

## Objectives

Extend the project with forecasting, portfolio optimization, and workflow automation.

### Modules Developed

### Moving Average Strategy

- 20-Day Moving Average
- 50-Day Moving Average
- Trend Identification

### Stock Forecasting

- Rolling Mean Forecast
- Trend Visualization

### Portfolio Optimization

- Risk vs Return Analysis
- Multi-stock comparison
- Portfolio diversification insights

### Automated Pipeline

- Automated execution of all analytics scripts
- Simplified workflow

---

## Outputs

- Moving Average Strategy Chart
- Stock Forecast Chart
- Portfolio Optimization Chart

---

# Skills Demonstrated

- Financial Data Analysis
- Data Cleaning & Preparation
- Exploratory Data Analysis (EDA)
- Time-Series Analysis
- Moving Average Analysis
- Rolling Volatility Analysis
- Risk & Return Analysis
- Portfolio Optimization
- Forecasting
- Interactive Dashboard Development
- KPI Design
- Data Visualization
- Power BI
- Python
- Git & GitHub

---

# Key Learnings

This project strengthened my understanding of:

- Financial Analytics
- Stock Market Analysis
- Quantitative Finance
- Business Intelligence
- Dashboard Storytelling
- Data Engineering for BI
- Portfolio Risk Analysis
- Forecasting Techniques
- End-to-End Analytics Workflow

---

# Future Improvements

- Machine Learning-based Stock Prediction
- Real-time Stock Market API Integration
- Sharpe Ratio & CAPM Analysis
- Portfolio Allocation Optimization
- Real-time Power BI Dashboard
- Predictive Analytics using LSTM/Prophet
- Interactive Web Dashboard using Streamlit

---