import psycopg2
from psycopg2 import sql
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), ".env")
load_dotenv(env_path)

DB_HOST = os.getenv("POSTGRES_HOST")
DB_PORT = "5432"
DB_NAME = os.getenv("POSTGRES_DB_NAME")
DB_USER = os.getenv("POSTGRES_USER")
DB_PASSWORD = os.getenv("POSTGRES_PASSWORD")

create_table_query = """
CREATE TABLE IF NOT EXISTS stocks (
    id SERIAL PRIMARY KEY,
    stock_name VARCHAR(255) NOT NULL, 
    stock_price DOUBLE PRECISION NOT NULL, 
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
); 
"""

def create_table(): 

    try: 
        conn = psycopg2.connect(
            host=DB_HOST, 
            port=DB_PORT, 
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD 
        )
        cur = conn.cursor()
        cur.execute(create_table_query)
        conn.commit()
        cur.close()
        conn.close()
    
    except Exception as e: 
        print("Error while creating table: ", e)
        
if __name__ == "__main__": 
    create_table()
    