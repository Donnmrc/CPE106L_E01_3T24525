from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
import sqlite3
import bcrypt
from pathlib import Path

DB_PATH = Path(__file__).parent / "MindfulBalance.db"
app = FastAPI()

class RegisterRequest(BaseModel):
    username: str
    password: str

class MoodRequest(BaseModel):
    username: str
    mood: str
    tags: list[str]

class JournalRequest(BaseModel):
    username: str
    content: str

def get_connection():
    return sqlite3.connect(DB_PATH)

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password: str, hashed: str) -> bool:
    return bcrypt.checkpw(password.encode(), hashed.encode())

def get_user_id(username: str) -> int:
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()
    if result:
        return result[0]
    raise HTTPException(status_code=404, detail="User not found")

@app.on_event("startup")
def startup():
    from backend.database import initialize_database
    initialize_database()

@app.post("/register")
def register_user(req: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        hashed = hash_password(req.password)
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)", (req.username, hashed))
        conn.commit()
        return {"message": "User registered successfully"}
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Username already exists")
    finally:
        conn.close()

@app.post("/login")
def login_user(req: RegisterRequest):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT password_hash FROM users WHERE username = ?", (req.username,))
    result = cursor.fetchone()
    conn.close()

    if result and verify_password(req.password, result[0]):
        return {"message": "Login successful"}
    else:
        raise HTTPException(status_code=401, detail="Invalid credentials")

@app.post("/mood")
def log_mood(req: MoodRequest):
    user_id = get_user_id(req.username)
    timestamp = datetime.now().isoformat()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO mood_entries (user_id, mood, tags, timestamp) VALUES (?, ?, ?, ?)",
        (user_id, req.mood, ",".join(req.tags), timestamp)
    )
    conn.commit()
    conn.close()
    return {"message": "Mood logged"}

@app.post("/journal")
def save_journal(req: JournalRequest):
    user_id = get_user_id(req.username)
    timestamp = datetime.now().isoformat()
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO journal_entries (user_id, content, timestamp) VALUES (?, ?, ?)",
        (user_id, req.content, timestamp)
    )
    conn.commit()
    conn.close()
    return {"message": "Journal entry saved"}

@app.get("/recommendation")
def get_recommendation(username: str):
    user_id = get_user_id(username)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT mood FROM mood_entries WHERE user_id = ? ORDER BY timestamp DESC LIMIT 5",
        (user_id,)
    )
    moods = [row[0] for row in cursor.fetchall()]
    conn.close()

    if moods.count("stressed") >= 3:
        return {"strategy": "Try a breathing exercise or journaling prompt."}
    elif moods.count("sad") >= 3:
        return {"strategy": "Listen to uplifting music or talk to a friend."}
    else:
        return {"strategy": "Keep tracking your mood. You're doing great!"}

@app.get("/stats")
def get_stats(username: str):
    user_id = get_user_id(username)
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT mood, COUNT(*) FROM mood_entries WHERE user_id = ? GROUP BY mood",
        (user_id,)
    )
    stats = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    return {"mood_stats": stats}
