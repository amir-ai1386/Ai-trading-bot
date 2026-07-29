import sqlite3
from datetime import datetime

DB_NAME = "signals.db"


def get_connection():
    return sqlite3.connect(DB_NAME)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS trades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        symbol TEXT NOT NULL,
        timeframe TEXT NOT NULL,
        signal TEXT NOT NULL,
        entry REAL,
        stop_loss REAL,
        tp1 REAL,
        tp2 REAL,
        tp3 REAL,
        status TEXT DEFAULT 'OPEN',
        confidence INTEGER,
        created_at TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()


def save_trade(symbol, timeframe, signal, entry=None, stop_loss=None, tp1=None, tp2=None, tp3=None, confidence=0):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO trades (
        symbol, timeframe, signal, entry, stop_loss, tp1, tp2, tp3, status, confidence, created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        symbol,
        timeframe,
        signal,
        entry,
        stop_loss,
        tp1,
        tp2,
        tp3,
        "OPEN",
        confidence,
        datetime.utcnow().isoformat()
    ))

    conn.commit()
    conn.close()
