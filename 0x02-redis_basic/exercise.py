#!/usr/bin/env python3
'''exercice module'''

import redis
import uuid


class Cache:
    '''Representation of a cache instance'''

    def __init__(self):
        '''Initializes a new Cache instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> uuid.UUID:
        '''Generates a random key using uuid as a key to store the data in the
        Redis storage'''
        k = str(uuid.uuid4())
        self._redis.set(k, data)
        return k
