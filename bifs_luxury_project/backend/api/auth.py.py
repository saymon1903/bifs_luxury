from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from fastapi import Depends, HTTPException, status
from sqlmodel import Session, select
from services.db import get_session
from api.models import User

SECRET = "CHANGE_ME"
ALGO = "HS256"
pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_pw(pw: str) -> str:
    return pwd_ctx.hash(pw)

def verify_pw(pw, hashed) -> bool:
    return pwd_ctx.verify(pw, hashed)

def create_token(user_id: int, admin: bool) -> str:
    to_encode = {"sub": str(user_id), "adm": admin,
                "exp": datetime.utcnow() + timedelta(hours=8)}
    return jwt.encode(to_encode, SECRET, ALGO)

async def get_current(session: Session = Depends(get_session),
                      token: str = Depends(lambda x: x.headers["Authorization"].split()[1])):
    cred_exc = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Bad creds")
    try:
        payload = jwt.decode(token, SECRET, ALGO)
        uid = int(payload["sub"])
    except (JWTError, KeyError):
        raise cred_exc
    user = session.exec(select(User).where(User.id == uid)).first()
    if not user:
        raise cred_exc
    return user
