from sqlalchemy import Column,String,Integer,ForeignKey
from sqlalchemy.orm import relationship
from .session import Base

class User(Base):
    __tablename__="users"
    
    id=Column(Integer,primary_key=True,index=True)
    username=Column(String(50),unique=True,index=True,nullable=False)
    hashed_password=Column(String(255),nullable=False)
    
    notes=relationship("note",back_populates="Owner")

class Note(Base):
    __tablename__="notes"
    
    id=Column(Integer,primary_key=True,index=True)
    title = Column(String(50), nullable=False)
    content = Column(String(255), nullable=False)
    user_id=Column(Integer,ForeignKey("users.id"))
    
    owner=relationship("user",back_populates="notes")
    