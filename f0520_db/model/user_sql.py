from config import config

# 회원리스트 - select
def selectAll_users():
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    conn.close()

    # sqlite3.Row를 사용했기 때문에 결과를 딕셔너리 형태
    return [dict(user) for user in users]

# 회원1명 - select
def select_user(user_id:int):
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users where id=?",(user_id,)) #튜플 쉼표 있어야 함
    user = cursor.fetchone()
    conn.close()
    
    if user is None:
        return None

    # sqlite3.Row를 사용했기 때문에 결과를 딕셔너리 형태
    return dict(user)


# 회원1명저장 - insert
def create_user(user_id:int,name:str,email:str):
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (id, name, email) VALUES (?, ?, ?)",
        (user_id, name, email)
    )
    conn.commit()
    conn.close()
    
    print("데이터 저장성공")
    
    return {
        "id": user_id,"name": name,"email": email
    }
    
# 회원1명수정 - update
def update_user(user_id:int,name:str,email:str):
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE users SET name = ?, email = ? WHERE id = ?",
        (name, email, user_id)
    )
    conn.commit()
    updated_count = cursor.rowcount  # 없을경우
    conn.close()

    if updated_count == 0:
        return None
    
    return {
        "id": user_id,"name": name,"email": email
    }
    
# 회원1명삭제 - delete
def delete_user(user_id:int):
    conn = config.get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM users WHERE id = ?", (user_id,)
    )
    conn.commit()
    updated_count = cursor.rowcount  # 없을경우
    conn.close()

    if updated_count == 0:
        return None
    
    return { "id": user_id }