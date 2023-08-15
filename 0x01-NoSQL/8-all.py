#!/usr/bin/env python3

'''8-all module'''


def list_all(mongo_collection):
    '''
    Lists all the documents of a MongoDB collection
    Arg:
        mongo_collection: a MongoDB Collection
    Return:
        a Python list of collection's documents if any
    '''
    return mongo_collection.find()
