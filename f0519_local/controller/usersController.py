from fastapi import APIRouter, HTTPException
import sqlite3
from model import user_sql


router = APIRouter(
    prefix="/users",
    tags= ["users"],
    responses={404:{"description":"페이지 없음"}},
)

# 임시 사용자 데이터
fake_users = [
    {"id": 1, "name": "홍길동", "email": "hong@test.com"},
    {"id": 2, "name": "김철수", "email": "kim@test.com"},
]

# 여러개 검색 - get
@router.get("/")
def read_user():
    # 03. 임시파일에 저장
    return {"users":fake_users}
    
    # 02.config -> user_sql.py 연결
    # users = user_sql.find_all_users()
    # return {"users":users}
    
    # 01.직접연결방법
    # conn = sqlite3.connect("project01.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users")
    # users = cursor.fetchall()
    # conn.close()
    # return {"users":users}

# 1개 검색 - get
@router.get("/{user_id}")
def read_user(user_id:str):
    return {"user_id":user_id}


# 저장 - POST 
@router.post("/")
def create_user(name: str, email: str):
    new_user = {
        "id": len(fake_users) + 1,
        "name": name,
        "email": email
    }
    print("신규 : ",new_user)
    fake_users.append(new_user)

    return {
        "message": "사용자가 생성되었습니다.",
        "user": new_user
    }

# 수정 - put
@router.put("/{user_id}")  # 수정
def update_user(user_id: int, name: str, email: str):
    print("수정페이지")
    for user in fake_users:
        if user["id"] == user_id:
            user["name"] = name
            user["email"] = email

            return {
                "message": "사용자 정보가 수정되었습니다.",
                "user": user
            }

    return {
        "message": "해당 사용자를 찾을 수 없습니다."
    }

# DELETE /users/1
@router.delete("/{user_id}")
def delete_user(user_id: int):
    for user in fake_users:
        if user["id"] == user_id:
            fake_users.remove(user)
            return {
                "message": "사용자가 삭제되었습니다.",
                "deleted_user": user
            }

    raise HTTPException(
        status_code=404,
        detail="삭제할 사용자를 찾을 수 없습니다."
    )


