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

    # Prepare the result
    result = {
        "predicted_yield": float(predicted_yield),  # Convert np.float64 to float
        "market_price": float(market_data['price']),  # Convert np.float64 to float
        "demand_index": float(market_data['demand']),  # Convert np.float64 to float
        "sustainability_score": float(sustainability_score),  # Convert np.float64 to float
        "weather_comment": weather_comment  # String
    }

    print("✅ Prediction result:", result)
    return result
