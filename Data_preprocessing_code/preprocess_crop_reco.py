import pandas as pd
from sklearn.preprocessing import StandardScaler
import os

os.makedirs("../../processed_data", exist_ok=True)

# Load dataset
df_crop = pd.read_csv("C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\data\\crop_recommendation.zip")

# Fill missing values
df_crop.fillna(method='ffill', inplace=True)

# Scale numerical features
scaler = StandardScaler()
df_crop[['N','P','K','temperature','humidity','ph','rainfall']] = scaler.fit_transform(
    df_crop[['N','P','K','temperature','humidity','ph','rainfall']]
)

# Save preprocessed file
df_crop.to_csv("../../processed_data/crop_recommendation_preprocessed.csv", index=False)

print("✅ Crop Recommendation dataset preprocessing done & saved to processed_data/crop_recommendation_preprocessed.csv")
