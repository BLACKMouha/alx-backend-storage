#!/usr/bin/python3
'''10-update_topics module'''


def update_topics(mongo_collection, name, topics):
    '''
    Puts topics approached in a school base on the school name
    Args:
        mongo_collection: a MongoDB Collection
        name: name of the school
        topics: list of strings
    Return:
        Nothing
    '''
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
