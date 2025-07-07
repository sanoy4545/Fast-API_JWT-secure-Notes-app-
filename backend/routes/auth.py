from fastapi import APIRouter,Depends,HTTPException,status
from datetime import timedelta
from sqlalchemy.orm import Session
from core.jwt import create_token
from passlib.context import CryptContext
from schemas import UserCreate,Token,UserLogin
from db.models import User
from db.session import session_local


router= APIRouter()
pwd_context= CryptContext(schemes=["bcrypt"],deprecated="auto")

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()
    
@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db) ):
    if db.query(User).filter(User.username==user.username).first():
        raise HTTPException(status_code=400,detail="User already exists")
    hashed= pwd_context.hash(user.password)
    new_user= User(username=user.username,hashed_password=hashed)
    db.add(new_user)
    db.commit()
    return {"msg":"user added"}

@router.post("/login",response_model=Token)
def login(user: UserLogin, db: Session = Depends(get_db) ):
    db_user = db.query(User).filter(User.username==user.username).first()
    if not db_user or not pwd_context.verify(user.password,db_user.hashed_password):
        raise HTTPException(status_code=400,detail="Invalid credentials")
    token=create_token(data={"sub": user.username}, expires_delta=timedelta(minutes=30))
    return {"access_token":token,"token_type":"bearer"}