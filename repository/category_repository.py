from sqlalchemy.orm import Session
from models.category_model import Category


class CategoryRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def get_category_by_id(self, category_id):
        return self.db_session.query(Category).filter(id == category_id).first()