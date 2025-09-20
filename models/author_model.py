from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base


class AuthorModel(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    books = relationship("BookModel", back_populates="author", cascade="all, delete-orphan")
