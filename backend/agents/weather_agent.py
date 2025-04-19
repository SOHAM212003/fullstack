class WeatherAgent:
    def assess_impact(self, temperature, rainfall):
        if temperature > 35:
            return "High heat stress expected."
        elif rainfall < 50:
            return "Water scarcity likely."
        return "Weather conditions are favorable."
