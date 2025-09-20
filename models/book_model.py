
from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from models.base import Base
class BookModel(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    # Foreign key linking to AuthorModel
    author_id = Column(Integer, ForeignKey("authors.author_id"), nullable=False)
    author = relationship("AuthorModel", back_populates="books")
    category_id = Column(Integer, ForeignKey("category.category_id"), nullable=False)
    category = relationship("Category", back_populates="books")

    def __init__(self, book_id, title, author, category):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.category = category
        self.author = author