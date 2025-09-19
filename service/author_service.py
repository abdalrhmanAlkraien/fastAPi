from dependency_injector.wiring import inject

from models.author_model import AuthorModel as Author
from repository.author_repository import AuthorRepository
from schema.request.AuthorRequest import AuthorRequest


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def create_author(self, authorRequest:AuthorRequest):
        author = Author()
        for key, value in authorRequest.model_dump().items():
            setattr(author, key, value)
        self.author_repository.create_author(author)

    def delete_author(self, author_id:int):
        self.author_repository.get_author_by_id(author_id)

    def update_author(self, author_id: int, data:AuthorRequest):
        self.author_repository.update_author(author_id, data)

    def find_author_by_name(self, name:str):
        return self.author_repository.get_author_by_name(name)

    def find_author_by_id(self, author_id:int):
        return self.author_repository.get_author_by_id(author_id)

    def find_all_author(self):
        return self.author_repository.find_all_author()

