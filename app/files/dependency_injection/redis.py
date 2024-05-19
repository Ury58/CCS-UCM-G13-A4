#app/files/dependency_injection/redis.py

from app.files.persistence.redis import RedisClient

def get_redis_client() -> RedisClient:
    return RedisClient()
