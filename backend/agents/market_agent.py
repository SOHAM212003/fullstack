import pandas as pd

class MarketAgent:
    def __init__(self, dataset_path='backend/data/market_researcher_dataset.csv'):
        self.market_data = pd.read_csv(dataset_path)

    def analyze_market(self, crop_type):
        crop_info = self.market_data[self.market_data['Product'] == crop_type]
        if crop_info.empty:
            return {"price": None, "demand": None}
        avg_price = crop_info['Market_Price_per_ton'].mean()
        avg_demand = crop_info['Demand_Index'].mean()
        return {"price": avg_price, "demand": avg_demand}
