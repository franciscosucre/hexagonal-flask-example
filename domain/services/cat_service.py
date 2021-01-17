from typing import List

from domain.entities.cat import Cat
from infrastructure.repositories.cat_repository import CatRepository


class CatService:
    cat_repository: CatRepository

    def __init__(self, cat_repository: CatRepository):
        self.cat_repository = cat_repository

    def find_all_cats(self) -> List[Cat]:
        return self.cat_repository.find_cats()

    def create_cat(self, cat: Cat) -> Cat:
        return self.cat_repository.create_cat(cat=cat)
