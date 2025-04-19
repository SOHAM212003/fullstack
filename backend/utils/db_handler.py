import sqlite3

class DBHandler:
    def __init__(self, db_path='backend/database/memory.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        query = '''
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farm_id TEXT,
            crop_type TEXT,
            predicted_yield REAL,
            market_price REAL,
            demand_index REAL,
            sustainability_score REAL,
            weather_comment TEXT
        )
        '''
        self.conn.execute(query)
        self.conn.commit()

    def insert_record(self, record):
        query = '''
        INSERT INTO recommendations
        (farm_id, crop_type, predicted_yield, market_price, demand_index, sustainability_score, weather_comment)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        '''
        self.conn.execute(query, record)
        self.conn.commit()
