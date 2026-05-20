from fastapi import APIRouter

router = APIRouter(
    prefix="/member",
    tags=["member"],
    responses={404: {"description": "페이지 없음"}},
)

# 회원 데이터 - 로컬파일연결
data_member = [
    {"id":1, "name":"홍길동", "email":"aaa@test.com"},
    {"id":2, "name":"유관순", "email":"bbb@test.com"},
    {"id":3, "name":"이순신", "email":"ccc@test.com"},
]

# 회원 전체 조회
@router.get("/")
def selectAll_member():
    return {"member":data_member}

# 회원 개별 조회 127.0.0.1:8000/member/1
@router.get("/{id}")
def selectOne_member(id:int):
    for item in data_member:
        if item["id"] == id:
            return {"member":item}
    return {"message":"해당 회원이 없습니다."}

# 회원 등록
@router.post("/")
def insert_member(item:dict):
    print("데이터 : ",item)
    data_member.append(item)
    return {
        "message":"회원 등록이 완료되었습니다.",
        "member":item
    }    



