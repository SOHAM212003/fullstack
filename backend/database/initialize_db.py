import sqlite3
import os

def initialize_database(db_path='backend/database/memory.db'):
    # Ensure the folder exists
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS recommendations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            farm_id TEXT,
            crop_type TEXT,
            predicted_yield REAL,
            market_price REAL,
            demand_index REAL,
            sustainability_score REAL,
            weather_comment TEXT,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
    print(f"Database initialized at {db_path}")

if __name__ == "__main__":
    initialize_database()
