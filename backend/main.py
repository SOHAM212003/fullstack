def run_system_with_data(farm_data):
    from agents.farmer_agent import FarmerAgent
    from agents.advisor_agent import AdvisorAgent
    from agents.market_agent import MarketAgent
    from agents.weather_agent import WeatherAgent
    from agents.sustainability_agent import SustainabilityAgent
    from utils.db_handler import DBHandler

    # Initialize agents
    farmer = FarmerAgent(farm_data)
    advisor = AdvisorAgent()
    market = MarketAgent()
    weather = WeatherAgent()
    sustainability = SustainabilityAgent()
    db = DBHandler()

    # Gather inputs
    data = farmer.provide_data()
    predicted_yield = advisor.predict_yield(data)
    market_data = market.analyze_market(data['Crop_Type'])
    sustainability_score = sustainability.assess_sustainability(data)
    weather_comment = weather.assess_impact(data['Temperature_C'], data['Rainfall_mm'])

    # Store results
    db.insert_record((
        data['Farm_ID'],
        data['Crop_Type'],
        predicted_yield,
        market_data['price'],
        market_data['demand'],
        sustainability_score,
        weather_comment
    ))

    result = {
        "predicted_yield": round(predicted_yield, 2),
        "market_price": round(market_data['price'], 2),
        "demand_index": round(market_data['demand'], 2),  # ✅ updated key
        "sustainability_score": round(sustainability_score, 2),
        "weather_comment": weather_comment
    }

    print("✅ Prediction result:", result)
    return result
