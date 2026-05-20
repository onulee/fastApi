import sqlite3
from pathlib import Path

# 프로젝트 루트 경로
BASE_DIR = Path(__file__).resolve().parent.parent

# DB 파일 경로
DB_PATH = BASE_DIR/"project01.db"

# db 커넥션
def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # db를 딕셔너리 형태로 리턴 
    return conn