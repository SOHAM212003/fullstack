import React from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import { CircularProgressbar, buildStyles } from 'react-circular-progressbar';
import 'react-circular-progressbar/dist/styles.css';

const ResultPage = () => {
  const navigate = useNavigate();
  const location = useLocation();
  const result = location.state?.result;

  // Defensive fallback
  if (!result || typeof result !== 'object') {
    return (
      <div className="flex items-center justify-center h-screen text-red-600 font-semibold text-lg">
        No prediction data available. Please submit the form again.
      </div>
    );
  }

  // Convert everything to safe numbers
  const predictedYield = parseFloat(result.predicted_yield) || 0;
  const sustainabilityScore = parseFloat(result.sustainability_score) || 0;
  const marketPrice = parseFloat(result.market_price) || 0;
  const demandIndex = parseFloat(result.demand_index) || 0;
  const weatherComment = typeof result.weather_comment === 'string' ? result.weather_comment : 'N/A';

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-green-50 to-white p-4">
      <div className="p-6 rounded-xl bg-white shadow-2xl space-y-6 w-full max-w-xl animate-fade-in transition-all duration-500">
        <h3 className="text-3xl font-bold text-center text-green-700 mb-4">Prediction Results</h3>

        <div className="grid grid-cols-2 gap-8">
          <div className="flex flex-col items-center">
            <CircularProgressbar
              value={predictedYield}
              maxValue={100}
              text={`${predictedYield}t`}
              styles={buildStyles({
                textColor: '#16a34a',
                pathColor: '#16a34a',
                trailColor: '#d1fae5',
              })}
            />
            <p className="mt-2 font-medium text-gray-700">Predicted Yield</p>
          </div>

          <div className="flex flex-col items-center">
            <CircularProgressbar
              value={sustainabilityScore}
              maxValue={100}
              text={`${sustainabilityScore}%`}
              styles={buildStyles({
                textColor: '#0284c7',
                pathColor: '#0284c7',
                trailColor: '#e0f2fe',
              })}
            />
            <p className="mt-2 font-medium text-gray-700">Sustainability Score</p>
          </div>
        </div>

        <div className="text-gray-700 text-sm space-y-2 px-2">
          <p><strong>Market Price:</strong> ₹{marketPrice.toFixed(2)}</p>
          <p><strong>Demand Index:</strong> {demandIndex.toFixed(2)}</p>
          <p><strong>Weather Insight:</strong> {weatherComment}</p>
        </div>

        <div className="flex justify-center">
          <button
            onClick={() => navigate('/')}
            className="mt-4 px-6 py-2 bg-green-600 text-white font-semibold rounded hover:bg-green-700 transition"
          >
            Submit Another
          </button>
        </div>

        {/* Safely render JSON data */}
        <div>
          <pre className="text-xs bg-gray-100 p-2 rounded">{JSON.stringify(result, null, 2)}</pre>
        </div>
      </div>
    </div>
  );
};

export default ResultPage;
