// src/App.jsx
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import FormPage from './components/FormPage';
import ResultPage from './components/ResultPage';

function App() {
  return (
    <Router>
      <div>
        <h1>Welcome to Sustainable Farming</h1>
        <Routes>
          <Route path="/" element={<FormPage />} />
          <Route path="/results" element={<ResultPage />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
