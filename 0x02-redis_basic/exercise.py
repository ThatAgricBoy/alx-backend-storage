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
