# app/auth/router.py

from fastapi import APIRouter, Body, Header
from hashlib import sha256
from random import randint
import redis

router = APIRouter()

@router.delete("/{id}")
async def test2(id: int) -> dict[str, int]:
    return {"id": id}

users = {}
redis_instance = redis.Redis(host="redis-dock", port=6379, decode_response=True)


@router.post("/register")
async def register_func(input: dict = Body()):
    user = input["user"]
    password = input["pass"]
    hash_password = user + password
    users[user] = sha256(hash_password.encode()).digest()
    return {}

@router.post("/login")
async def login_func(input: dict = Body()) -> dict:
    user = input["user"]
    password = sha256((user + input["pass"]).encode()).digest()
    print(user)
    print(password)
    print(password == users[user])
    token = randint(0,100000000)
    redis.set(token, user)
    return {"token": token}

@router.get("/introspect")
async def introspect_func(token: str = Header()):
    print(token)
    return {}


