# app/persistence/token.py

import redis
import json

class TokenPersistence:
    def __init__(self):
        self.redis_instance = redis.Redis(host="redis-dock", port=6379, decode_responses=True)

    def set_token(self, token: int, user_info: dict):
        self.redis_instance.set(token, json.dumps(user_info))

    def get_token(self, token: int) -> dict:
        user_info_json = self.redis_instance.get(token)
        if user_info_json:
            return json.loads(user_info_json)
        return None
    
    def delete_token(self, token: int):
        self.redis_instance.delete(token)

# Initialize the persistence instance
token_persistence = TokenPersistence()
