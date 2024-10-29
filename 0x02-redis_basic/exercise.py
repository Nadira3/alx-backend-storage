#!/usr/bin/env python3

import redis
import uuid
from typing import Union


class Cache:
    """ class that creates a cache """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database on initialization

    def store(self, data: Union[str, bytes, int, float]) -> str:
        key = str(uuid.uuid4())  # Generate a unique key
        self._redis.set(key, data)  # Store the data in Redis
        return key  # Return the key as a string
