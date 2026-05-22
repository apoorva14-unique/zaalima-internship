import pandas as pd

# Load dataset
df = pd.read_csv("../../data/raw/Retail.csv", encoding='latin1')

# Check missing values
print("Missing values:")
print(df.isnull().sum())

# Remove duplicate rows
df = df.drop_duplicates()

# Convert Date column
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Fill missing values
df.fillna(method='ffill', inplace=True)

# Save cleaned dataset
df.to_csv("../../data/raw/cleaned_stock_data.csv", index=False)

print("Data cleaning completed")