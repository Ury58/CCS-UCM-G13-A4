# app/auth/api/router.py

from fastapi import APIRouter, Body, Header
from hashlib import sha256
from random import randint
import json
from app.auth.persistence.token import token_persistence

router = APIRouter()

@router.delete("/{id}")
async def test2(id: int) -> dict[str, int]:
    return {"id": id}

users = {}

@router.post("/register")
async def register_func(input: dict = Body()):
    user = input["user"]
    password = input["pass"]
    hash_password = sha256((user + password).encode()).digest()
    
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
        
        token_persistence.set_token(token, introspect_user)
        return {"token": token}
    else:
        return {"error": "Invalid credentials"}

@router.get("/introspect")
async def introspect_func(token: str = Header()) -> dict:
    user_info = token_persistence.get_token(token)
    if user_info:
        return user_info
    else:
        return {"error": "Invalid token"}


