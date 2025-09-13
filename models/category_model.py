from sqlalchemy import Column, ForeignKey, Integer, String

from models.base import Base
from models.book_model import BookModel


class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = list(BookModel)
