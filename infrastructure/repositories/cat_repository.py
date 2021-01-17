from typing import List, Optional

from domain.entities.cat import Cat
from infrastructure.mongodb_adapter import MongoDbAdapter


class CatRepository:
    collection_name: str = 'cats'

    def __init__(self, mongodb: MongoDbAdapter):
        self.mongodb = mongodb

    def find_cats(self) -> List[Cat]:
        raw_cats = self.mongodb.find(
            collection_name=self.collection_name,
        )
        return list(map(lambda c: Cat(**c), raw_cats))

    def find_cats_by_id(self, cat_id: str) -> Optional[Cat]:
        raw_cat = self.mongodb.find_one(
            collection_name=self.collection_name,
            conditions=dict(id=cat_id)
        )
        return Cat(**raw_cat) if raw_cat else None
