from dependency_injector.wiring import inject

from error.RepositoryError import RepositoryError
from models.author_model import AuthorModel as Author
from repository.author_repository import AuthorRepository
from schema.request.AuthorRequest import AuthorRequest
from schema.response.AuthorResponse import AuthorResponse


class AuthorService:
    def __init__(self, author_repository: AuthorRepository):
        self.author_repository = author_repository

    def create_author(self, authorRequest:AuthorRequest):
        author = Author()
        for key, value in authorRequest.model_dump().items():
            setattr(author, key, value)
        self.author_repository.create_author(author)

    def delete_author(self, author_id:int):
        self.author_repository.delete_author(author_id)

    def update_author(self, author_id: int, data:AuthorRequest):
        author = Author()
        for key, value in data.model_dump().items():
            setattr(author, key, value)
        self.author_repository.update_author(author_id, author)

    def find_author_by_name(self, name:str):
        return self.author_repository.get_author_by_name(name)

    def find_author_by_id(self, author_id:int):
        author = self.author_repository.get_author_by_id(author_id)

        if author is None:
            raise RepositoryError(f"Failed to find author with id: {author_id}")
        else:
            return AuthorResponse(
                author_id=author.author_id,
                name=author.name,
                age=author.age,
        )

    def find_all_author(self) -> list[AuthorResponse]:
        author_list =  self.author_repository.find_all_author()
        response = []

        for model in author_list:
            response.append(AuthorResponse(
                author_id=model.author_id,
                name=model.name,
                age=model.age,
            ))
        return response

