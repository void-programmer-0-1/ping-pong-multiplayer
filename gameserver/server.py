from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from auth import hash_password, verify_password, create_access_token, decode_access_token
from models import RegisterRequest, LoginRequest, LoginResponse
from database import UserDatabaseUtils

server = FastAPI()
user_db_util = UserDatabaseUtils()

server.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


@server.post("/register", status_code=201)
async def register(request: RegisterRequest):
    hashed_password = hash_password(request.password)
    try:
        user_db_util.create_user(username=request.username,email=request.email,password=hash_password)
        return {"status": "200", "response":"User Registered Successfully"}
    except Exception as err:
        print("USER REGISTER LOG::{}".format(str(err)))
        return HTTPException(status_code=400,detail="User already exists")


@server.post("/login", status_code=200)
async def login(request: LoginRequest):
    user = await user_db_util.get_user_by_email_id(request.email)
    if not user or not verify_password(plain_password=request.password, hashed_password=user["password"]):
        raise HTTPException(status_code=400, details="Invalid User Credentials")
    
    access_token = create_access_token(data={"user_id": user["id"]})
    return LoginResponse(access_token=access_token, token_type="bearer")


@server.get("/")
async def home_route(request: Request, token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)

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


@server.get("/pong-game")
async def game_route(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="game.html"
    )






