from database.connection import engine
from models.base import Base

Base.metadata.create_all(bind=engine)