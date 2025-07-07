from jose import jwt,JWTError
from typing import Union
from datetime import datetime,timedelta
from .config import settings

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

def create_token(data: dict, expires_delta: Union[timedelta,None] = None):
    to_encode= data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({'exp':expire})
    return jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)

def verify_token(token: str):
    try:
        payload=jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None