import jwt
from passlib.context import CryptContext
from datetime import datetime, timedelta

# TODO port this to env variables
# and read it from there
SECRET_KEY = "12345"
ALGORITHM = "HS256"
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expires_delta = datetime.utcnow() + (expires_delta or timedelta(minutes=30))
    to_encode.update({"expire": expires_delta})
    return jwt.encode(to_encode, SECRET_KEY, ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise ValueError("Token has expired")
    except jwt.JWTError:
        raise ValueError("Invalid Token")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


