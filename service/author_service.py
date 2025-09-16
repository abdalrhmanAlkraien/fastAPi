from dependency_injector.wiring import inject

from models.author_model import AuthorModel as Author
from repository.author_repository import AuthorRepository


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    @inject
    def create_author(self, user:Author):
        self.author_repository.get_author_by_id(user.id)

    def delete_author(self, author_id:int):
        self.author_repository.get_author_by_id(author_id)