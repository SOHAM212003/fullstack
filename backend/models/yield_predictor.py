import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Load the dataset
df = pd.read_csv('backend/data/farmer_advisor_dataset.csv')

# Feature set and target variable
X = df[['Soil_pH', 'Soil_Moisture', 'Temperature_C', 'Rainfall_mm', 'Fertilizer_Usage_kg', 'Pesticide_Usage_kg']]
y = df['Crop_Yield_ton']

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
os.makedirs('models', exist_ok=True)
with open('backend/models/yield_predictor.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Yield predictor model saved at models/yield_predictor.pkl")
