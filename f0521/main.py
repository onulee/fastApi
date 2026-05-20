from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from controller import memberController

app = FastAPI()
app.include_router(memberController.router)

# static 파일 연결
app.mount("/static", StaticFiles(directory="static"), name="static")
# template 파일 연결
templates = Jinja2Templates(directory="templates")

@app.get("/")
def root(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html", 
        context={"request": request,"id":1 }
    )