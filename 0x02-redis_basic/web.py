#!/usr/bin/env python3
'''web module'''

import requests
from typing import Callable
import redis
from functools import wraps


cache = redis.Redis()


def count_requests(func: Callable) -> Callable:
    '''Counts the number of requests of an URL'''
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        '''Calls func with its arguments'''
        cache.incr(f'count:{url}')
        return func(url, *args, **kwargs)
    return wrapper


def cache_content(func: Callable) -> Callable:
    '''Caches the content of a web page for 10 seconds'''
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        '''Calls func with its arguments'''
        key = f'cached:{url}'
        content = cache.get(key)
        if content:
            return content.decode('utf-8')
        content = func(url, *args, **kwargs)
        cache.setex(key, 10, content if content else '')
        return content
    return wrapper


@count_requests
@cache_content
def get_page(url: str) -> str:
    '''Gets a page'''
    return requests.get(url).text
