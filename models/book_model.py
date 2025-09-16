
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from models.base import Base
class BookModel(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)


    def __init__(self, title, author):
        self.title = title
        self.author = author