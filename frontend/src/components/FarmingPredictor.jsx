import React, { useState } from 'react';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

const initialForm = {
  farm_id: '',
  soil_ph: '',
  soil_moisture: '',
  temperature: '',
  rainfall: '',
  crop_type: '',
  fertilizer_usage: '',
  pesticide_usage: '',
};

const FarmingPredictor = () => {
  const [formData, setFormData] = useState(initialForm);
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const data = await response.json();
      console.log("Backend response:", data); // Debugging log
      setResult(data);
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
    setLoading(false);
  };

  const handleReset = () => {
    setResult(null);
    setFormData(initialForm);
  };

  if (result) {
    console.log("Received result:", result); // Debugging log

    const predictedYield = parseFloat(result.predicted_yield) || 0;
    const sustainabilityScore = parseFloat(result.sustainability_score) || 0;
    const marketPrice = parseFloat(result.market_price) || 0;
    const demandIndex = parseFloat(result.demand_index) || 0;
    const weatherComment = result.weather_comment || 'N/A';

    return (
      <div>
        <h3>Prediction Results</h3>
        <p>Predicted Yield: {predictedYield}t</p>
        <p>Sustainability Score: {sustainabilityScore}%</p>
        <p>Market Price: ₹{marketPrice.toFixed(2)}</p>
        <p>Demand Index: {demandIndex.toFixed(2)}</p>
        <p>Weather Insight: {weatherComment}</p>
      </div>
    );
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-2xl font-bold mb-4 text-center text-green-700">Sustainable Farming Predictor</h1>
      <form onSubmit={handleSubmit} className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-3xl mx-auto bg-white p-6 shadow-lg rounded-lg">
        {Object.entries(formData).map(([key, value]) => (
          <div key={key} className="flex flex-col">
            <label htmlFor={key} className="text-gray-700 capitalize mb-1">{key.replace(/_/g, ' ')}</label>
            <input
              type={key === 'crop_type' ? 'text' : 'number'}
              id={key}
              name={key}
              value={value}
              onChange={handleChange}
              required
              className="p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-green-400 text-sm"
              placeholder={`Enter ${key.replace(/_/g, ' ')}`}
            />
          </div>
        ))}
        <div className="md:col-span-2 flex justify-center">
          <button
            type="submit"
            className="bg-green-600 text-white px-6 py-2 rounded-md hover:bg-green-700 transition-all duration-300"
            disabled={loading}
          >
            {loading ? 'Predicting...' : 'Predict'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default FarmingPredictor;
