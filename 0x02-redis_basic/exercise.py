#!/usr/bin/env python3
'''exercice module'''

import redis
import uuid
from typing import Union, Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    '''Counts how many times methods of Cache class are called'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Calls the method with its arguments'''
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    '''Tracks a function call input paramters and outputs'''
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        '''Call the function with its arguments'''
        self._redis.rpush(method.__qualname__ + ':inputs', str(args))
        r = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ':outputs', str(r))
        return r
    return wrapper


def replay(method: Callable) -> None:
    call_histories = redis.Redis()
    name = method.__qualname__
    inputs = call_histories.lrange(name + ':inputs', 0, -1)
    outputs = call_histories.lrange(name + ':outputs', 0, -1)
    print(f'{name} was called {len(inputs)} times:')
    for i, o in zip(inputs, outputs):
        print(f'{name}(*{i.decode("utf-8")}) -> {o.decode("utf-8")}')


class Cache:
    '''Representation of a cache instance'''

    def __init__(self):
        '''Initializes a new Cache instance'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''Generates a random key using uuid as a key to store the data in the
        Redis storage'''
        k = str(uuid.uuid4())
        self._redis.set(k, data)
        return k

    def get(self, key: str, fn: Callable = None):
        '''Retrieves and Converts to the rigth the data based on the key'''
        if key is None:
            return None
        data = self._redis.get(key)
        return fn(data) if fn else data if data else None

    def get_str(self, key: str) -> str:
        '''Retrieves and stringfies data corresponding the key'''
        return str(self._redis.get(key))

    def get_int(self, key: str) -> int:
        '''Retrieves and converts into an integer the data based on the key'''
        try:
            return int(self._redis.get(key))
        except Exception as e:
            return None
