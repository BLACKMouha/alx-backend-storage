#!/usr/bin/env python3

"""8-main module test"""

from pymongo import MongoClient

list_all = __import__('8-all').list_all

if __name__ == '__main__':
    client = MongoClient()
    db = client.my_db
    school_collection = db.school
    schools = list_all(school_collection)
    for school in schools:
        print('[{}] {}'.format(school.get('_id', None),
                               school.get('name', None)))
