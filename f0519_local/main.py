from fastapi import FastAPI
from controller import itemsController, usersController, memberController

app = FastAPI()
app.include_router(itemsController.router)
app.include_router(usersController.router)
app.include_router(memberController.router)

@app.get("/")
def read_root():
    return {"main":"메인페이지_로컬:딕셔너리파일"}



