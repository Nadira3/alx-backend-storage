#!/usr/bin/env python3

import redis
import uuid
from typing import Any, Optional, Union


class Cache:
    """ class that creates a cache """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database on initialization

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key  # Return the key as a string

    def get(self, key: str, fn) -> Optional[Any]:
        """Retrieve value by key and apply the conversion function."""
        return fn(self._redis.get(key))

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve string value by key."""
        value = self._redis.get(key)
        return value.decode() if value else None

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve integer value by key."""
        value = self._redis.get(key)
        return int(value) if value is not None else None
