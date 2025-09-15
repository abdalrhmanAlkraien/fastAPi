from models.author_model import AuthorModel as Author
class AuthorService:
    def __init__(self):
        print(" init called")

    def create_author(self, user:Author):
        print(self)

    def delete_author(self, author_id:int):
        print(self, "delete author {}".format(id))