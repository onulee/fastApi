from fastapi import APIRouter, HTTPException
import sqlite3
from model import user_sql

router = APIRouter(
    prefix="/users", tags= ["users"],
    responses={404:{"description":"페이지 없음"}},
)

# 여러개 검색 - get
@router.get("/")
def read_user():
    # 02.db 연결-config.py
    users = user_sql.selectAll_users()
    return {"users":users}
    
    # 01.직접연결방법 - 리스트타입
    # conn = sqlite3.connect("project01.db")
    # cursor = conn.cursor()
    # cursor.execute("SELECT * FROM users")
    # users = cursor.fetchall()
    # conn.close()
    # return {"users":users}

# 1개 검색 - get
@router.get("/{user_id}")
def read_user(user_id:str):
    user = user_sql.select_user(user_id)
    print("user : ",user)
    if user is None:
        return {"message": "사용자를 찾을 수 없습니다."}
    return {"user":user}


# 저장 - POST 
@router.post("/{user_id}")
def create_user(user_id:int, name: str, email: str):
    user = user_sql.create_user(user_id,name,email)

    return {
        "message": "사용자가 추가되었습니다.",
        "user": user
    }

# 수정 - put
@router.put("/{user_id}")  # 수정
def update_user(user_id: int, name: str, email: str):
    user = user_sql.update_user(user_id,name,email)
    
    if user is None:
        return {
            "message": "해당 사용자를 찾을 수 없습니다."
        }
    
    return {
        "message": "사용자 정보가 수정되었습니다.",
        "user": user
    }


# DELETE /users/1
@router.delete("/{user_id}")
def delete_user(user_id: int):
    user = user_sql.delete_user(user_id)
    
    if user is None:
        return {
            "message": "해당 사용자를 찾을 수 없습니다."
        }
    
    return {
        "message": "사용자 정보가 삭제되었습니다.",
        "user": user
    }

    

