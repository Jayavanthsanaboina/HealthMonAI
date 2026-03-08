import sqlite3

DB_NAME = "data/health.db"

def connect():
    return sqlite3.connect(DB_NAME)

def create_tables():

    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medication(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        time TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS health_metrics(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        steps INTEGER,
        heart_rate INTEGER,
        date TEXT
    )
    """)

    conn.commit()
    conn.close()