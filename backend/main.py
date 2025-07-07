from db.session import engine,Base
import db.models
from fastapi import FastAPI
from routes import auth

app=FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)



