from models.book_model import BookModel as Book

class BookService:

    def create_book(self, book: Book):
        print(self)

    def delete_book(self, book_id:int):
        print(self, "delete book {}".format(book_id))