#!/usr/bin/env python3
"""Redis exercise"""

import redis
import uuid
from typing import Union


class Cache:
    def __init__(self, host='localhost', port=6379, db=0):
        """Initialize Redis instance"""
        self._redis = redis.Redis(host, port, db)
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis"""
        key = str(uuid.uuid4())
        self._redis.mset({key: data})
        return key
    
    def get(self, key: str, fn: callable = None) -> Union[str, bytes, int, float]:
        """Get data from Redis"""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data
        # BEGIN: qv9d5c3jw3d4
        def count_calls(method: callable) -> callable:
            """Decorator to count method calls"""
            counts = {}

            def wrapper(self, *args, **kwargs):
                key = method.__qualname__
                counts[key] = counts.get(key, 0) + 1
                return method(self, *args, **kwargs)

            return wrapper
        # END: qv9d5c3jw3d4
    
    def get_str(self, key: str) -> str:
        """Convert data to string"""
        return self.get(key, str)
    
    def get_int(self, key: str) -> int:
        """Convert data to int"""
        return self.get(key, int)
    
    def get_str_list(self, key: str) -> list:
        """Convert data to list of strings"""
        return self.get(key, lambda d: [s.decode('utf-8') for s in d])
    
    def get_int_list(self, key: str) -> list:
        """Convert data to list of ints"""
        return self.get(key, lambda d: [int(s.decode('utf-8')) for s in d])
    