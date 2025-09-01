import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv

env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(env_path)

def connect_db(): 
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"), 
        port="5432", 
        dbname=os.getenv("POSTGRES_DB_NAME"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"), 
        connect_timeout=5
    )
    return conn

def ping(): 
    try :
        with connect_db() as conn: 
            with conn.cursor() as cur: 
                cur.execute("SELECT 1;")
                cur.fetchone()
        return True, None
    except Exception as e:
        return False, str(e)

def read_from_db(query, params=None): 
    with connect_db() as conn: 
        with conn.cursor(cursor_factory=RealDictCursor) as cursor: 
            cursor.execute(query, params)
            return cursor.fetchall()

def fetch_all(): 
    return read_from_db("SELECT * FROM stocks;")

