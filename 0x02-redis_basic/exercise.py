#!/usr/bin/env python3

import redis
import uuid
from typing import Optional, Union, Callable
from typing import Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Use `method.__qualname__` as a unique key to track call count
        key = method.__qualname__
        self._redis.incr(key)  # Increment the call count
        return method(self, *args, **kwargs)  # Call the original method
    return wrapper

def call_history(method: Callable) -> Callable:
    """ decorator to store the history of inputs and outputs for a particular function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))
        
        res = method(self, *args, **kwargs)  # Call the original method
        
        self._redis.rpush(output_key, res)
        return res
    return wrapper

class Cache:
    """ Class that creates a cache. """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database on initialization

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key  # Return the key as a string

    def get(self, key: str, fn: Optional[Callable] = None)\
            -> Optional[Union[str, int]]:
        """Retrieve value by key and optionally
            apply the conversion function."""
        value = self._redis.get(key)
        if fn and value is not None:
            return fn(value)
        return value

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve string value by key."""
        return self.get(key, lambda x: x.decode() if x else None)

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve integer value by key."""
        return self.get(key, lambda x: int(x) if x is not None else None)
