from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

server = FastAPI()

server.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@server.get("/")
async def home_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )



