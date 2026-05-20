from config import config

def find_all_users():
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # sqlite3.Row를 사용했기 때문에 결과를 딕셔너리 형태
    return [dict(user) for user in users]