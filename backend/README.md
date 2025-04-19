# 🌾 Data-Driven AI for Sustainable Farming
**Gen AI Sprint Hackathon — Powered by Data**

A multi-agent AI system that empowers farmers to make sustainable, profitable, and data-informed decisions by collaborating with weather stations and agricultural experts. Our solution reduces environmental impact, optimizes crop yield, and adapts to market trends using AI and long-term memory with SQLite.

---

## 🔍 Problem Statement

> Agriculture is vital to human survival, but unsustainable practices lead to soil degradation, water scarcity, and high carbon emissions. The challenge is to build a collaborative AI system involving farmers, weather data, and market intelligence — promoting eco-friendly, profitable farming decisions.

---

## 🧠 Our Solution: Multi-Agent AI System

We developed an intelligent, modular system that simulates collaboration between:

- 👨‍🌾 **Farmer Agent** – Inputs crop preferences, land data, and budget.
- 🤖 **Advisor Agent** – Uses ML models to predict crop yield and sustainability.
- 📊 **Market Researcher Agent** – Analyzes market data to suggest profitable crops.
- 🌦️ **Weather Station Agent** – Shares weather impact scores and rainfall predictions.

All agents share a common **SQLite memory (`memory.db`)** for persistent collaboration.

---

## 🧱 Project Structure

![Structure](https://raw.githubusercontent.com/SOHAM212003/sustainable_farming_ai/main/presentation/structure.png)

---

## 📊 Datasets Used

1. **farmer_advisor_dataset.csv**  
   Features: Soil pH, Moisture, Temperature, Rainfall, Fertilizer & Pesticide usage, Crop Yield, Sustainability Score

2. **market_researcher_dataset.csv**  
   Features: Product, Price per ton, Demand/Supply Index, Weather & Seasonal Factors, Consumer Trend Index

---

## 🧠 Machine Learning Models

| Model                     | Type               | Output                         | File                          |
|--------------------------|--------------------|--------------------------------|-------------------------------|
| Yield Predictor          | Linear Regression  | Predicts `Crop_Yield_ton`      | `models/yield_predictor.pkl` |
| Sustainability Predictor | Random Forest      | Predicts `Sustainability_Score`| `models/sustainability_model.pkl` |

Train using:

```bash
python models/train_yield_model.py
python models/train_sustainability_model.py

---
## 💡 Key Features

✅ Multi-agent system for collaborative decision-making
✅ Predictive models for yield and sustainability
✅ Market-aware crop recommendation
✅ SQLite long-term memory for agent context
✅ Scalable, modular code structure

---

##🌍 Impact & Benefits

🌱 Promotes sustainable farming (low pesticide, optimal water usage)
📈 Helps farmers choose profitable crops based on real market trends
🧠 Boosts decision-making using AI-driven collaboration
📉 Reduces carbon footprint and soil erosion

---
##📌 Future Enhancements

Integrate live weather APIs
Add crop disease prediction using image input
Deploy as a web-based advisor portal (Streamlit/FastAPI)
Introduce LLM-powered Natural Language Farmer Interface

---
##🛠 Tech Stack

Python, SQLite, Pandas, Scikit-learn
Modular agent-based architecture
Git, GitHub, Git LFS (for large model files)

---
