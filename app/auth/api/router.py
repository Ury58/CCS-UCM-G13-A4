# app/auth/api/router.py

from fastapi import APIRouter, Body, Header
from hashlib import sha256
from random import randint
import redis
import json

router = APIRouter()

@router.delete("/{id}")
async def test2(id: int) -> dict[str, int]:
    return {"id": id}

users = {}
redis_instance = redis.Redis(host="redis-dock", port=6379, decode_responses=True)

@router.post("/register")
async def register_func(input: dict = Body()):
    user = input["user"]
    password = input["pass"]
    hash_password = sha256((user + password).encode()).digest()
    
    # Add additional user info if needed
    user_info = {
        "name": input.get("name", ""),
        "surname": input.get("surname", ""),
        "password": hash_password  # Store the hashed password
    }
    users[user] = user_info
    return {}

@router.post("/login")
async def login_func(input: dict = Body()) -> dict:
    user = input["user"]
    password = sha256((user + input["pass"]).encode()).digest()
    
    if user in users and password == users[user]["password"]:
        token = randint(0, 100000000)
        
        introspect_user = {
            "user_id": user,
            "name": users[user]["name"]
        }
        
        redis_instance.set(token, json.dumps(introspect_user))
        return {"token": token}
    else:
        return {"error": "Invalid credentials"}

@router.get("/introspect")
async def introspect_func(token: str = Header()) -> dict:
    user_info_json = redis_instance.get(token)
    if user_info_json:
        return json.loads(user_info_json)
    else:
        return {"error": "Invalid token"}
    



