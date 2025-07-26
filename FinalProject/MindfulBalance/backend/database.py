# database.py
import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).parent / "MindfulBalance.db"

def get_connection():
    return sqlite3.connect(DB_PATH)

def initialize_database():
    conn = get_connection()
    cursor = conn.cursor()

    # Create tables with proper constraints
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL UNIQUE,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS journal_entries (
        entry_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS mood_logs (
        mood_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        mood_level INTEGER NOT NULL CHECK(mood_level BETWEEN 1 AND 10),
        notes TEXT,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(user_id)
    )
    """)

    # Add coping strategies if table is empty
    cursor.execute("SELECT COUNT(*) FROM coping_strategies")
    if cursor.fetchone()[0] == 0:
        cursor.executemany(
            "INSERT INTO coping_strategies (title, description, category) VALUES (?, ?, ?)",
            [
                ("Deep Breathing", "Inhale for 4 seconds, hold for 4, exhale for 6", "Anxiety"),
                ("Gratitude Journal", "Write 3 things you're grateful for", "Depression"),
                ("Nature Walk", "Spend 10 minutes outside", "Stress")
            ]
        )

    conn.commit()
    conn.close()
