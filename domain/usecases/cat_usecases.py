from domain.entities.cat import Cat
from domain.services.cat_service import CatService


class CatUseCase:
    cat_service: CatService

    def __init__(self, cat_service: CatService):
        self.cat_service = cat_service

    def find_all_cats(self):
        return self.cat_service.find_all_cats()

    def create_cat(self, cat: Cat):
        return self.cat_service.create_cat(cat=cat)
