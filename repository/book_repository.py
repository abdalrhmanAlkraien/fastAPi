from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from error.RepositoryError import RepositoryError
from models.book_model import BookModel as Book

class BookRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def find_all(self):
        return self.db_session.query(Book).all()

    def find_by_id(self, book_id:int):
        return self.db_session.query(Book).get(book_id)

    def find_by_name(self, book_name:str):
        return self.db_session.query(Book).filter(Book.name == book_name).first()

    def create_book(self, book:Book):
        self.db_session.add(book)

    def update_book(self, book:Book) -> type[Book] | None:
        currentBook = self.db_session.query(Book).filter(Book.id == book.id).first()

        if currentBook is None:
            return None
        else:
            try:
                for key, value in book.items():
                    setattr(currentBook, key, value)
                self.db_session.add(currentBook)
                self.db_session.commit()
                self.db_session.refresh(currentBook)
                return currentBook

            except SQLAlchemyError as e:
                self.db_session.rollback()
                raise RepositoryError(f"Failed to update book: {e}") from e

    def delete_book(self, book_id:int) -> None:
        self.db_session.query(Book).filter(Book.id == book_id).delete()
        self.db_session.commit()
        self.db_session.refresh(Book)

    def get_book_by_id(self, book_id):
        return self.db_session.query(Book).filter(id == book_id).first()