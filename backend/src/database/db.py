import psycopg2
from psycopg2.extras import RealDictCursor

def connection():
    try:
        conn = psycopg2.connect(
            dbname="patocash",
            user="root",
            password="root",
            host="postgres",
            port="5432"
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
