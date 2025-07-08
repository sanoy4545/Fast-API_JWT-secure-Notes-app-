from pydantic import BaseModel
from typing import Union

class UserCreate(BaseModel):
    username: str
    password: str

class UserLogin(UserCreate):
     pass

class TokenData(BaseModel):
    username: Union[str,None] = None

class Token(BaseModel):
    access_token: str
    token_type: str

class NoteCreate(BaseModel):
    title: str
    content: str

class NoteUpdate(BaseModel):
    title: Union[str,None] = None
    content: Union[str,None] = None