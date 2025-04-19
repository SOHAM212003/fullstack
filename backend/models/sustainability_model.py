import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import pickle
import os

# Load dataset
df = pd.read_csv('backend/data/farmer_advisor_dataset.csv')

# Feature set and target variable
X = df[['Soil_pH', 'Soil_Moisture', 'Temperature_C', 'Rainfall_mm', 'Fertilizer_Usage_kg', 'Pesticide_Usage_kg']]
y = df['Sustainability_Score']

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X, y)

# Save model
os.makedirs('models', exist_ok=True)
with open('backend/models/sustainability_model.pkl', 'wb') as f:
    pickle.dump(model, f)

print("✅ Sustainability model saved at models/sustainability_model.pkl")
