# backend/app.py
from flask import Flask, request, jsonify
from flask_cors import CORS
from main import run_system_with_data

app = Flask(__name__)
CORS(app)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        print("📩 Received farm data:", data)

        farm_data = {
            'Farm_ID': data['farm_id'],
            'Soil_pH': float(data['soil_ph']),
            'Soil_Moisture': float(data['soil_moisture']),
            'Temperature_C': float(data['temperature']),
            'Rainfall_mm': float(data['rainfall']),
            'Crop_Type': data['crop_type'],
            'Fertilizer_Usage_kg': float(data['fertilizer_usage']),
            'Pesticide_Usage_kg': float(data['pesticide_usage']),
        }

        result = run_system_with_data(farm_data)
        return jsonify(result)

    except Exception as e:
        print("❌ Error in prediction:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    print("🚀 Starting backend on http://localhost:5000")
    app.run(debug=True, port=5000)
