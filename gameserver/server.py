from fastapi import (
    FastAPI, Request, Depends, 
    HTTPException, status
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import ValidationError



server = FastAPI()
server.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@server.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc: RequestValidationError):
    error_details = [
        {"message": err["msg"]}
        for err in exc.errors()
    ]
    print(error_details)
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content={"status": "error", "errors": error_details},
    )


@server.get("/")
async def home_route(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@server.get("/about")
async def about_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="about.html"
    )

@server.get("/room")
async def room_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="room.html"
    )


@server.get("/game")
async def game_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="game.html"
    )






