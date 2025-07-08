from fastapi import Depends,HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from core.jwt import verify_token
from jose import JWTError
from schemas import TokenData

oauth2_scheme= OAuth2PasswordBearer(tokenUrl="/login")

def get_user(token : str = Depends(oauth2_scheme)):
    payload=verify_token(token)
    if not payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    username = payload.get("sub")
    if username is None:
        raise HTTPException(status_code=400, detail="Token missing subject (sub)")
    return username

