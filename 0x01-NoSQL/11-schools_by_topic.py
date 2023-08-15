#!/usr/bin/env python3

'''11-schools_by_topic module'''


def schools_by_topic(mongo_collection, topic):
    '''
    Finds the school that approach a set of topic
    Args:
        mongo_collection: a MongoDB collection
        topic: a list of strings, representing each one a topic
    Return: a list of schools that have the list of topics in their topics
    '''
    return mongo_collection.find({'topics': topic})
