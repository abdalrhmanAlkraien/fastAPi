from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from error.RepositoryError import RepositoryError
from models.author_model import AuthorModel as Author
from typing import Any

from schema.request.AuthorRequest import AuthorRequest


class AuthorRepository:

    def __init__(self, db_session: Session):
        self.db_session = db_session

    def create_author(self, author: Author) -> None:
        try:
            self.db_session.add(author)
            self.db_session.commit()
            self.db_session.refresh(author)
        except SQLAlchemyError as e:
            self.db_session.rollback()
            raise RepositoryError(f"Failed to create author: {e}") from e

    def update_author(self, author_id, new_val: AuthorRequest) -> type[Author] | None:

        author = self.db_session.query(Author).filter(id == author_id).first()
        if author is None:
            return None
        else:
            try:
                # update value.
                for key, value in new_val.items():
                    setattr(author, key, value)
                self.db_session.commit()
                self.db_session.refresh(author)
                return author
            except SQLAlchemyError as e:
                self.db_session.rollback()
                raise RepositoryError(f"Failed to update author: {e}") from e

    def delete_author(self, author_id: int) -> None:
        author = self.db_session.query(Author).filter(id == author_id).first()
        if author is None:
            return None
        else:
            try:
                self.db_session.delete(author)
                self.db_session.commit()
                self.db_session.refresh(author)
                return None
            except SQLAlchemyError as e:
                self.db_session.rollback()
                raise RepositoryError(f"Failed to delete author: {e}") from e

    def get_author_by_id(self, author_id):
        return self.db_session.query(Author).filter(id == author_id).first()

    def get_author_by_name(self, name: str):
        exp : Any = Author.name == name
        return self.db_session.query(Author).filter(exp).first()

    def find_all_author(self):
        return self.db_session.query(Author).all()