from sqlalchemy import Column, Integer, String, ForeignKey

from models.base import Base
from models.book_model import BookModel


class AuthorModel(Base):
    __tablename__ = 'authors'
    name = Column(String, primary_key=True)
    age = Column(Integer)
    books = list[BookModel]

    def __init(self, name, age, books):
        self.name = name
        self.age = age
        self.books = books