from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base import Base
from models.book_model import BookModel


class Category(Base):
    __tablename__ = 'category'
    category_id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("BookModel", back_populates="category", cascade="all, delete-orphan")