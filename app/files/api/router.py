#app/files/api/router.py

import os
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from pydantic import BaseModel
from typing import List, Dict
from fastapi.responses import FileResponse
from app.files.domain.services import FileService, get_file_service
from app.files.dependency_injection.redis import get_redis_client
from app.files.persistence.redis import RedisClient

router = APIRouter()

file_names = {}

@router.get("/file")
async def get_file(service: FileService = Depends(get_file_service)) -> dict:
    files = service.get_all_files("dummy_user")
    return {"files": files}

@router.post("/file")
async def post_file(input: dict, service: FileService = Depends(get_file_service)) -> dict:
    id = len(file_names)
    name = input["name"]
    file_names[name] = id
    return {"id": id}

@router.get("/file/{id}")
async def get_file(id: int, service: FileService = Depends(get_file_service)):
    for current_name, current_id in file_names.items():
        if current_id == id:
            filename = current_name
    return FileResponse(filename, media_type="application/pdf", filename=filename)

@router.post("/file/merge")
async def merge_files(input: dict, service: FileService = Depends(get_file_service)) -> dict:
    merged_file = service.merge_files("dummy_user", input["files"])
    return {"id": merged_file["id"]}

@router.post("/file/{id}")
async def post_file(id: int, file: UploadFile = File(), service: FileService = Depends(get_file_service)) -> dict:
    result = service.update_file("dummy_user", id, file) 
    return result

@router.delete("/file/{id}")
async def delete_file(id: int, service: FileService = Depends(get_file_service)) -> dict:
    result = service.delete_file("dummy_user", id)
    return result
