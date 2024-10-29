#!/usr/bin/env python3

import redis
import uuid
from typing import Optional, Union, Callable


class Cache:
    """ Class that creates a cache. """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database on initialization

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
