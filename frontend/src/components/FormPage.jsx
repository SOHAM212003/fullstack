import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function FormPage() {
  const [formData, setFormData] = useState({
    farm_id: '',
    soil_ph: '',
    soil_moisture: '',
    temperature: '',
    rainfall: '',
    crop_type: '',
    fertilizer_usage: '',
    pesticide_usage: '',
  });

  const navigate = useNavigate();

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await fetch('http://127.0.0.1:5000/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(formData),
      });
      const result = await response.json();
      navigate('/results', { state: { result } });
    } catch (error) {
      console.error('Error fetching prediction:', error);
    }
  };

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
          >
            Predict
          </button>
        </div>
      </form>
    </div>
  );
}

export default FormPage;
