from models.book_model import BookModel as Book
from repository.book_repository import BookRepository


class BookService:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def create_book(self, book: Book):
        print(self)

    def delete_book(self, book_id:int):
        print(self, "delete book {}".format(book_id))