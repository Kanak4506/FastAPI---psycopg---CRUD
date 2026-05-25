import psycopg2

from psycopg2.extras import RealDictCursor


def get_connection():
    conn = psycopg2.connect(
        host="localhost",
        database="forPythonBackend",
        user="postgres",
        password="4506",
        cursor_factory=RealDictCursor,  # converts rows into dictionaries , by default it return tuples
    )

    return conn
