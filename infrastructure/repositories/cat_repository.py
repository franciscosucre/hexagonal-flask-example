from typing import List, Optional, Dict

from domain.entities.cat import Cat
from infrastructure.mongodb_adapter import MongoDbAdapter


class CatRepository:
    collection_name: str = 'cats'

    def __init__(self, mongodb: MongoDbAdapter):
        self.mongodb = mongodb

    def find_cats(self) -> List[Cat]:
        raw_cats: List[Dict] = self.mongodb.find(
            collection_name=self.collection_name,
        )
        return list(map(lambda c: self._restore(document=c), raw_cats))

    def find_cats_by_id(self, cat_id: str) -> Optional[Cat]:
        raw_cat: Dict = self.mongodb.find_one(
            collection_name=self.collection_name,
            conditions=dict(id=cat_id)
        )
        return self._restore(**raw_cat) if raw_cat else None

    def create_cat(self, cat: Cat) -> Cat:
        raw_cat: Dict = self.mongodb.insert_one(
            collection_name=self.collection_name,
            document=self._adapt(cat=cat)
        )
        return self._restore(document=raw_cat) if raw_cat else None

    def _restore(self, document: Dict) -> Cat:
        return Cat(
            id=document['id'],
            name=document['name']
        )

    def _adapt(self, cat: Cat) -> Dict:
        return {
            'id': cat.id,
            'name': cat.name
        }
