from db.session import engine,Base
import db.models

Base.metadata.create_all(bind=engine)
