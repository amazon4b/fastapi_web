from fastapi import FastAPI ,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def main(request: Request):
    return templates.TemplateResponse(request=request,name="index.html", context={"name":"이미옥"})


@app.get('/hello/{name}', response_class=HTMLResponse)
async def hello(request: Request, name):
    words = f'당신의 이름은 {name}이니깐 반가워서 인사'
    return templates.TemplateResponse(request=request,name="hello.html", context={"name":words})