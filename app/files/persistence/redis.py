#app/files/persistence/redis.py

import redis

class RedisClient:
    def __init__(self):
        self.client = redis.Redis(host="redis", port=6379, decode_responses=True)

    def set(self, key, value):
        self.client.set(key, value)

    def get(self, key):
        return self.client.get(key)
