from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
import os

ALGORITHM = "HS256"
SECRET = os.environ.get("SECRET_KEY")


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, SECRET, algorithms=[ALGORITHM])
        return decoded_token
    except:
        return {}
