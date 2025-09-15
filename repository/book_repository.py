from sqlalchemy.orm import Session
from models.book_model import BookModel as Book

class BookRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_book_by_id(self, book_id):
        return self.db_session.query(Book).filter(id == book_id).first()