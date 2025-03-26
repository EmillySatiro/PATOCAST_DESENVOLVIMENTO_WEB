import psycopg2
from psycopg2.extras import RealDictCursor
from datetime import datetime

def connection():
    try:
        conn = psycopg2.connect(
            dbname="patocash",
            user="root",
            password="root",
            host="localhost",
            port="5432"
        )
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
