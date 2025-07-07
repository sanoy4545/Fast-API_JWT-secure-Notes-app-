from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from core.jwt import verify_token
from jose import JWTError
from schemas import TokenData

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/login")

def get_user(token : str = Depends(oauth2_scheme)):
    payload=verify_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid Token")
    return payload.get("sub")

