import sqlite3

def init_db():
    conn = sqlite3.connect("mood_entries.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            emotion TEXT NOT NULL,
            sentiment TEXT NOT NULL,
            journal TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_entry(date, time, emotion, sentiment, journal):
    conn = sqlite3.connect("mood_entries.db")
    c = conn.cursor()
    c.execute('''
        INSERT INTO entries (date, time, emotion, sentiment, journal)
        VALUES (?, ?, ?, ?, ?)
    ''', (date, time, emotion, sentiment, journal))
    conn.commit()
    conn.close()

def fetch_entries():
    conn = sqlite3.connect("mood_entries.db")
    c = conn.cursor()
    c.execute('SELECT * FROM entries ORDER BY id DESC')
    rows = c.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    init_db()
