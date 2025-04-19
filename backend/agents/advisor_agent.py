import os
import pickle
import pandas as pd
import random

class AdvisorAgent:
    def __init__(self, model_path='backend/models/yield_predictor.pkl'):
        self.model = None
        self.is_mock = False

        if os.path.exists(model_path):
            try:
                with open(model_path, 'rb') as f:
                    self.model = pickle.load(f)
                print("✅ Loaded trained model from", model_path)
            except Exception as e:
                print("⚠️ Failed to load model, using mock prediction instead:", e)
                self.is_mock = True
        else:
            print(f"⚠️ Model file not found at {model_path}. Using mock prediction.")
            self.is_mock = True

    def predict_yield(self, farm_data):
        feature_dict = {
            'Soil_pH': [farm_data['Soil_pH']],
            'Soil_Moisture': [farm_data['Soil_Moisture']],
            'Temperature_C': [farm_data['Temperature_C']],
            'Rainfall_mm': [farm_data['Rainfall_mm']],
            'Fertilizer_Usage_kg': [farm_data['Fertilizer_Usage_kg']],
            'Pesticide_Usage_kg': [farm_data['Pesticide_Usage_kg']]
        }

        if self.is_mock or self.model is None:
            print("🤖 Using mock prediction based on input values...")
            # Simple mock formula
            yield_prediction = (
                20
                + farm_data['Soil_Moisture'] * 0.2
                + farm_data['Soil_pH'] * 0.3
                + farm_data['Rainfall_mm'] * 0.05
                + farm_data['Fertilizer_Usage_kg'] * 0.1
                + random.uniform(-3, 3)
            )
            return round(yield_prediction, 2)
        else:
            features_df = pd.DataFrame(feature_dict)
            return self.model.predict(features_df)[0]
