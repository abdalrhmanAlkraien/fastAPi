from sqlalchemy import ColumnElement, BinaryExpression
from sqlalchemy.orm import Session
from models.author_model import AuthorModel as Author
from typing import Any
class AuthorRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_author_by_id(self, author_id):
        return self.db_session.query(Author).filter(id == author_id).first()

    def get_author_by_name(self, name: str):
        exp : Any = Author.name == name
        return self.db_session.query(Author).filter(exp).first()