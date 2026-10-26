import os
import sqlite3

# 1. Hardcoded Secret / Token
API_KEY = "sk_live_1234567890abcdef12345678"

# 2. SQL Injection Vulnerability
def get_user_data(user_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE id = '{user_id}'"
    cursor.execute(query)
    return cursor.fetchall()

# 3. Command Injection / Insecure Subprocess
def run_backup(folder_name):
    os.system(f"tar -czf backup.tar.gz {folder_name}")
