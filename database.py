import sqlite3

def init_db():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            is_premium INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()

def add_user(user):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute('''
        INSERT OR IGNORE INTO users (user_id, username, first_name)
        VALUES (?, ?, ?)
    ''', (user.id, user.username, user.first_name))
    conn.commit()
    conn.close()

def set_premium(user_id, value=True):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("UPDATE users SET is_premium=? WHERE user_id=?", (int(value), user_id))
    conn.commit()
    conn.close()

def is_premium(user_id):
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT is_premium FROM users WHERE user_id=?", (user_id,))
    row = cur.fetchone()
    conn.close()
    return row and row[0] == 1

def get_all_users():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users")
    users = cur.fetchall()
    conn.close()
    return [u[0] for u in users]

def get_user_count():
    conn = sqlite3.connect("users.db")
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM users")
    count = cur.fetchone()[0]
    conn.close()
    return count
