#!/usr/bin/env python3

""" module containing redis functions """
import redis
import uuid
from typing import Optional, Union, Callable
from typing import Callable
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called."""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        # Use `method.__qualname__` as a unique key to track call count
        self._redis.incr(key)  # Increment the call count
        return method(self, *args, **kwargs)  # Call the original method
    return wrapper


def call_history(method: Callable) -> Callable:
    """ decorator to store the history of inputs and outputs of function """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        input_key = method.__qualname__ + ":inputs"
        output_key = method.__qualname__ + ":outputs"

        self._redis.rpush(input_key, str(args))

        res = method(self, *args, **kwargs)  # Call the original method

        self._redis.rpush(output_key, res)
        return res
    return wrapper


def replay(method):
    """ decorator to display the history of
        calls of a particular function """
    # 1. Define the qualified name
    qualname = method.__qualname__

    # 2. Define Redis keys for inputs and outputs
    input_key = f"{qualname}:inputs"
    output_key = f"{qualname}:outputs"

    # 3. Retrieve lists of inputs and outputs from Redis
    inputs = method.__self__._redis.lrange(input_key, 0, -1)
    outputs = method.__self__._redis.lrange(output_key, 0, -1)

    # 4. Print the total number of calls
    print(f"{qualname} was called {len(inputs)} times:")

    # 5. Loop over inputs and outputs together
    for input_val, output_val in zip(inputs, outputs):
        # Decode input and output values from Redis directly
        input_str = input_val.decode('utf-8')
        output_str = output_val.decode('utf-8')
        print(f"{qualname}(*{input_str}) -> {output_str}")


class Cache:
    """ Class that creates a cache. """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()  # Flush database on initialization

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ method to generate a random key (e.g. using uuid)
            store the input data in Redis using the random key
            and return the key """
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
