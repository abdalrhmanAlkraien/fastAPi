from repository.category_repository import CategoryRepository


class CategoryService:

    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def create_category(self, category_name:str):
        print(self, "create category")

    def delete_category(self, category_id:int):
        print(self, "delete category")