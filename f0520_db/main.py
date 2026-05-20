from fastapi import FastAPI
from controller import itemsController, usersController

app = FastAPI()
app.include_router(itemsController.router)
app.include_router(usersController.router)

@app.get("/")
def read_root():
    return {"main":"데이터 - db연결"}



