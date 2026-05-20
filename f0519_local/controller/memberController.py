from fastapi import APIRouter, HTTPException
import sqlite3


router = APIRouter(
    prefix="/member",
    tags= ["member"],
    responses={404:{"description":"페이지 없음"}},
)

# 임시 사용자 데이터
fake_users = [
    {"id": 1, "name": "홍길동", "email": "hong@test.com"},
    {"id": 2, "name": "김철수", "email": "kim@test.com"},
]

@router.get("/list")
def get_members():
    return {"users": fake_users}

    