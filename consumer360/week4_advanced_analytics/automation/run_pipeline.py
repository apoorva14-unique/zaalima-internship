import os

print("🚀 Starting Full Consumer360 Pipeline")

# Week 2 Pipeline
os.system("python consumer360/week2_analysis/data_pipeline/pipeline.py")

# Week 4 Market Basket
os.system("python consumer360/week4_advanced_analytics/market_basket/market_basket.py")

# Week 4 Cohort Analysis
os.system("python consumer360/week4_advanced_analytics/cohort_analysis/cohort_analysis.py")

print("✅ Full Pipeline Completed")