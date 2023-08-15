#!/usr/bin/env python3

'''9-insert_school module'''


def insert_school(mongo_collection, **kwargs):
    '''
    Inserts a new document inside a MongoDB collection
    Args:
        mongo_collection: a MongoDB Collection object
        kwargs: a dictionary
    Return:
        _id of the new document
    '''
    r = mongo_collection.insert_one(kwargs)
    return r.inserted_id
