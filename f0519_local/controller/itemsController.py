from fastapi import APIRouter

router = APIRouter(
    prefix="/items",
    tags= ["items"],
    responses={404:{"description":"페이지 없음"}},
)

@router.get("/{item_id}")
def read_item(item_id:int,name:str | None=None,id:str | None=None):
    return {"item_id":item_id,"name":name,"id":id}

@router.get("/aaa/{item_id}")
def read_item2():
    return {"sub":"2"}

