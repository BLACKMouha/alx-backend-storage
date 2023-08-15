#!/usr/bin/env python3

'''8-all module'''
from pymongo.collection import Collection
from pymongo.cursor import CursorType


def list_all(mongo_collection: Collection) -> CursorType:
    '''
    Lists all the documents of a MongoDB collection
    Arg:
        mongo_collection: a MongoDB Collection
    Return:
        a Python list of collection's documents if any
    '''
    return [] if mongo_collection.count == 0\
        else [doc for doc in mongo_collection.find()]
