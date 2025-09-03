import os
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Input file
input_file = "C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\data\\weather_data.csv"
df_weather = pd.read_csv(input_file)

# Preprocessing
df_weather = df_weather.drop_duplicates()
df_weather = df_weather.fillna(method='ffill')
df_weather = df_weather[(df_weather['Temperature_C'] >= 0) & (df_weather['Temperature_C'] <= 60)]

# Scaling
scaler = MinMaxScaler()
df_weather[['Temperature_C', 'Rainfall_mm', 'Humidity_%']] = scaler.fit_transform(
    df_weather[['Temperature_C', 'Rainfall_mm', 'Humidity_%']]
)

# Output folder (sirf folder ka path, file ka nahi)
output_folder = "C:\\Users\\guddu\\OneDrive\\Desktop\\Internship project\\processed_data"
os.makedirs(output_folder, exist_ok=True)

# Output file (folder + filename)
output_file = os.path.join(output_folder, "weather_processed.csv")

# Save
df_weather.to_csv(output_file, index=False)

print("✅ File saved at:", output_file)
