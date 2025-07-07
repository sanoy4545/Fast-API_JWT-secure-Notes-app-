from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from core.config import settings
from sqlalchemy.ext.declarative import declarative_base

database_url=settings.DATABASE_URL

engine=create_engine(database_url)

session_local=sessionmaker(autoflush=False,autocommit=False,bind=engine)
Base=declarative_base()