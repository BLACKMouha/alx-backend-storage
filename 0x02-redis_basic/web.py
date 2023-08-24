#!/usr/bin/env python3
'''web module'''

import requests
from typing import Callable
import redis
from functools import wraps


cache = redis.Redis()


def count_access(func: Callable) -> Callable:
    '''Counts how many times an url got accessed'''
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        '''Calls func with its arguments'''
        k = f'count:{url}'
        cache.incr(k, 1)
        return func(url, *args, **kwargs)
    return wrapper


def cache_content(func: Callable) -> Callable:
    '''Caches the content of a web page for 10 seconds'''
    @wraps(func)
    def wrapper(url, *args, **kwargs):
        '''Calls func with its arguments'''
        content = cache.get(url)
        if content:
            return content.decode('utf-8')
        content = func(url, *args, **kwargs)
        cache.setex(url, 10, content if content else '')
        return content
    return wrapper


@count_access
@cache_content
def get_page(url: str) -> str:
    '''Gets a page'''
    try:
        return requests.get(url).text
    except Exception as e:
        return None
