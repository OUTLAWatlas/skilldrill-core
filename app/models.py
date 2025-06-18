from flask import current_app

def get_connection():
    return current_app.db
def fetch_all_users():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM users"
    cursor.execute(query)
    results =   cursor.fetchall()
    cursor.close()
    return results
def insert_user(name, email, password):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, password))
    conn.commit
    cursor.close()