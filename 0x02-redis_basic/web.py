#!/usr/bin/env python3
'''web module'''

import requests
from typing import Callable
import redis
from functools import wraps


cache = redis.Redis()


def count_cache(func: Callable) -> Callable:
    '''Caches the content of a web page for 10 seconds'''
    @wraps(func)
    def wrapper(url):
        '''Calls func with its arguments'''
        cache.incr(f"count:{url}")
        content = cache.get(f"cached:{url}")
        if content:
            return content.decode('utf-8')
        content = func(url)
        cache.setex(f"cached:{url}", 10, content)
        return content

    return wrapper


@count_cache
def get_page(url: str) -> str:
    '''Gets a page'''
    return requests.get(url).text
