import pandas as pd
import os

os.makedirs("../../processed_data", exist_ok=True)

# Load dataset
df_market = pd.read_csv("C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\data\\market_price.csv")

# Handle missing values
df_market.fillna(method='ffill', inplace=True)

# Remove duplicates
df_market.drop_duplicates(inplace=True)

# Save preprocessed file
df_market.to_csv("C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\processed_data\\market_price_processed.csv", index=False)

print("✅ Market Price dataset preprocessing done & saved to processed_data/market_price_preprocessed.csv")
