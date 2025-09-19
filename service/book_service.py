from models.book_model import BookModel as Book
from repository.book_repository import BookRepository


class BookService:

    def __init__(self, book_repository: BookRepository):
        self.book_repository = book_repository

    def create_book(self, book: Book):
        self.book_repository.create_book(book)

    def delete_book(self, book_id:int):
        self.book_repository.delete_book(book_id)
    def get_book_by_id(self, book_id):
        self.book_repository.get_book_by_id(book_id)

    def update_book(self, book:Book):
        self.book_repository.update_book(book)

    def get_all_book(self):
        self.book_repository.find_all()
