#!/usr/bin/env python3
"""
Main file
"""
import redis

Cache = __import__('exercise').Cache

cache = Cache()

local_redis = redis.Redis()

data = b"Hello"
key = cache.store(data)
print(key)
print(local_redis.get(key))

data = 50
key = cache.store(data)
print(key)
print(local_redis.get(key))

data = 3.14
key = cache.store(data)
print(key)
print(local_redis.get(key))

data = "string"
key = cache.store(data)
print(key)
print(local_redis.get(key))
