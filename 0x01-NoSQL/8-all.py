#!/usr/bin/env python3

'''8-all module'''

from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.cursor import CursorType


def list_all(mongo_collection: Collection) -> CursorType:
    return [] if mongo_collection.count == 0\
        else [doc for doc in mongo_collection.find()]
