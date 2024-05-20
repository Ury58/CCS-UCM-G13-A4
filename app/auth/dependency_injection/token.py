#app/auth/dependency_injection/token.py

from app.auth.persistence.redis import RedisClient

def get_redis_client() -> RedisClient:
    return RedisClient()
