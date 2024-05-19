#app/files/api/router.py

from fastapi import APIRouter, HTTPException, UploadFile, File, Header, Body, Path
from pydantic import BaseModel
from typing import Optional, Union, List, Dict
from pypdf import PdfMerger

router = APIRouter()

@router.get("/file")
async def get_file() -> dict[str, Any]:
    files = []
    for name, id in file_names.items():
        files.append({"id": id, "name": name})
    return {"files": files}


@router.post("/file")
async def post_file(input: dict) -> dict[str, int]:
    id = len(file_names)
    name = input["name"]
    file_names[name] = id
    return {"id": id}


@router.get("/file/{id}")
async def get_file(id: int):
    for current_name, current_id in file_names.items():
        if current_id == id:
            filename = current_name
    return FileResponse(filename, media_type="application/pdf", filename=filename)


@router.post("/file/merge")
async def merge_files(input: dict) -> dict[str, int]:
    pdfs = []
    for current_name, current_id in file_names.items():
        if current_id in input["files"]:
            pdfs.append(current_name)
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)
    id = len(file_names)
    name = input["name"]
    merger.write(name)
    merger.close()
    file_names[name] = id
    return {"id": id}


@router.post("/file/{id}")
async def post_file(id: int, file: UploadFile = File()) -> dict[str, str]:
    for current_name, current_id in file_names.items():
        if current_id == id:
            filename = current_name
    with open(filename, "wb") as buffer:
        while chunk := await file.read(8192):
            buffer.write(chunk)
    return {}


@router.delete("/file/{id}")
async def delete_file(id: int) -> dict[str, str]:
    for current_name, current_id in file_names.items():
        if current_id == id:
            filename = current_name
    try:
        os.remove(filename)
    except Exception:
        pass
    del file_names[filename]
    return {}