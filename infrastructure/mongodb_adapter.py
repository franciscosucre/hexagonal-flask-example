from typing import Optional, Dict, List, Tuple

from pymongo import MongoClient, database

from enum import Enum

from pymongo.collection import Collection
from pymongo.cursor import Cursor
from pymongo.results import InsertManyResult, InsertOneResult
from typing import NewType


class SortDirection(Enum):
    ASCENDING = 1
    DESCENDING = -1


SortDirections = NewType('SortDirections', SortDirection)


class MongoDbAdapter:
    client: MongoClient
    db: database.Database

    def connect(self, uri: str):
        self.client = MongoClient(host=uri)
        self.db = self.client.get_default_database()

    def disconnect(self):
        self.client.close()
        self.client = None

    def find(
            self,
            collection_name: str,
            conditions: Optional[Dict] = None,
            projection: Optional[Dict] = None,
            limit: int = 0,
            skip: int = 0,
            sort: Optional[List[Tuple[str, SortDirections]]] = None
    ) -> List[Dict]:
        cursor: Cursor = self.get_collection(collection_name).find(
            filter=conditions,
            projection=projection,
            limit=limit,
            skip=skip,
            sort=sort,
        )
        return list(cursor)

    def find_one(self, collection_name: str, conditions: Optional[Dict] = None) -> Optional[Dict]:
        document: Optional[Dict] = self.get_collection(collection_name).find_one(filter=conditions)
        return document

    def count(self, collection_name: str, conditions: Optional[Dict] = None) -> int:
        return self.get_collection(collection_name).count_documents(
            filter=conditions,
        )

    def insert_one(self, collection_name: str, document: Dict) -> Dict:
        result: InsertOneResult = self.get_collection(collection_name).insert_one(
            document=document,
        )
        return self.find_one(collection_name=collection_name, conditions=dict(_id=result.inserted_id))

    def insert_many(
            self,
            collection_name: str,
            documents: List[Dict] = None,
    ) -> List[Dict]:
        result: InsertManyResult = self.get_collection(collection_name).insert_many(documents=documents)
        return self.find(collection_name=collection_name, conditions={'_id': {'$in': result.inserted_ids}})

    def get_collection(self, collection_name: str) -> Collection:
        return self.db.get_collection(collection_name)
