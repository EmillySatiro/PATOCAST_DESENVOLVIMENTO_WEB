import psycopg2
from os import getenv

def connection():
    try:
        conn = psycopg2.connect(
            dbname= getenv("POSTGRES_DB"),
            user= getenv("POSTGRES_USER"),
            password=getenv("POSTGRES_PASSWORD"),
            host=getenv("POSTGRES_HOST"),
            port=getenv("POSTGRES_PORT"),
        )
        print("Connected to the database")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
