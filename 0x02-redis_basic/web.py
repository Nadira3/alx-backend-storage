#!/usr/bin/env python3

import requests
import redis
from typing import Callable
from functools import wraps

# Initialize Redis client
redis_client = redis.Redis()

def cache_page(method: Callable) -> Callable:
    """
    Decorator that caches page content and tracks URL access count.
    """
    @wraps(method)
    def wrapper(url: str) -> str:
        # Redis keys for caching content and counting accesses
        cache_key = f"cache:{url}"
        count_key = f"count:{url}"

        # Increment the access count
        redis_client.incr(count_key)

        # Check if the URL content is cached
        cached_content = redis_client.get(cache_key)
        if cached_content:
            return cached_content.decode('utf-8')

        # Fetch the page content if not cached
        page_content = method(url)
        
        # Cache the content with an expiration of 10 seconds
        redis_client.setex(cache_key, 10, page_content)
        return page_content

    return wrapper

@cache_page
def get_page(url: str) -> str:
    """ Fetches HTML content of a given URL. """
    response = requests.get(url)
    return response.text
