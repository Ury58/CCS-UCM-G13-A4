#app/files/api/router.py

# # # from fastapi import APIRouter, HTTPException, UploadFile, File, Header, Body, Path
# # # from app.files.domain.services import get_file_service
# # # from app.auth.persistence.token import token_persistence
# # # from pydantic import BaseModel
# # # from typing import Optional, Union, List, Dict
# # # from pypdf import PdfMerger

# # # router = APIRouter()

# # # def validate_token(token: str):
# # #     user_info = token_persistence.get_token(token)
# # #     if not user_info:
# # #         raise HTTPException(status_code=401, detail="Invalid token")
# # #     return user_info

# # # @router.get("/file")
# # # async def get_file() -> dict[str, any]:
# # #     files = []
# # #     for name, id in file_names.items():
# # #         files.append({"id": id, "name": name})
# # #     return {"files": files}


# # # @router.post("/file")
# # # async def post_file(input: dict) -> dict[str, int]:
# # #     id = len(file_names)
# # #     name = input["name"]
# # #     file_names[name] = id
# # #     return {"id": id}


# # # @router.get("/file/{id}")
# # # async def get_file(id: int):
# # #     for current_name, current_id in file_names.items():
# # #         if current_id == id:
# # #             filename = current_name
# # #     return FileResponse(filename, media_type="application/pdf", filename=filename)


# # # @router.post("/file/merge")
# # # async def merge_files(input: dict) -> dict[str, int]:
# # #     pdfs = []
# # #     for current_name, current_id in file_names.items():
# # #         if current_id in input["files"]:
# # #             pdfs.append(current_name)
# # #     merger = PdfMerger()
# # #     for pdf in pdfs:
# # #         merger.append(pdf)
# # #     id = len(file_names)
# # #     name = input["name"]
# # #     merger.write(name)
# # #     merger.close()
# # #     file_names[name] = id
# # #     return {"id": id}


# # # @router.post("/file/{id}")
# # # async def post_file(id: int, file: UploadFile = File()) -> dict[str, str]:
# # #     for current_name, current_id in file_names.items():
# # #         if current_id == id:
# # #             filename = current_name
# # #     with open(filename, "wb") as buffer:
# # #         while chunk := await file.read(8192):
# # #             buffer.write(chunk)
# # #     return {}


# # # @router.delete("/file/{id}")
# # # async def delete_file(id: int) -> dict[str, str]:
# # #     for current_name, current_id in file_names.items():
# # #         if current_id == id:
# # #             filename = current_name
# # #     try:
# # #         os.remove(filename)
# # #     except Exception:
# # #         pass
# # #     del file_names[filename]
# # #     return {}

# # from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Header, Body
# # from typing import List
# # from app.files.domain.services import get_file_service, FileService
# # from app.auth.api.router import get_current_user

# # router = APIRouter()

# # @router.get("/files")
# # async def get_all_files(Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.get_all_files(user["user_id"])

# # @router.post("/files")
# # async def create_file(file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.upload_file(user["user_id"], file)

# # @router.get("/files/{file_id}")
# # async def get_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.get_file(user["user_id"], file_id)

# # @router.delete("/files/{file_id}")
# # async def delete_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.delete_file(user["user_id"], file_id)

# # @router.post("/files/{file_id}")
# # async def update_file(file_id: int, file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.update_file(user["user_id"], file_id, file)

# # @router.post("/files/merge")
# # async def merge_files(file_ids: List[int] = Body(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
# #     user = get_current_user(Authorization)
# #     if not user:
# #         raise HTTPException(status_code=401, detail="Invalid token")
# #     return file_service.merge_files(user["user_id"], file_ids)


# from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Header, Body
# from typing import List
# from app.files.domain.services import get_file_service, FileService
# from app.auth.api.router import get_current_user

# router = APIRouter()

# @router.get("/files")
# async def get_all_files(Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.get_all_files(user["user_id"])

# @router.post("/files")
# async def create_file(file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.upload_file(user["user_id"], file)

# @router.get("/files/{file_id}")
# async def get_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.get_file(user["user_id"], file_id)

# @router.delete("/files/{file_id}")
# async def delete_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.delete_file(user["user_id"], file_id)

# @router.post("/files/{file_id}")
# async def update_file(file_id: int, file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.update_file(user["user_id"], file_id, file)

# @router.post("/files/merge")
# async def merge_files(file_ids: List[int] = Body(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
#     user = get_current_user(Authorization)
#     if not user:
#         raise HTTPException(status_code=401, detail="Invalid token")
#     return file_service.merge_files(user["user_id"], file_ids)

from fastapi import APIRouter, Depends, HTTPException, UploadFile, File, Header, Body
from typing import List
from app.files.domain.services import get_file_service, FileService
from app.auth.api.router import get_current_user

router = APIRouter()

@router.get("/files")
async def get_all_files(Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.get_all_files(user["user_id"])

@router.post("/files")
async def create_file(file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.upload_file(user["user_id"], file)

@router.get("/files/{file_id}")
async def get_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.get_file(user["user_id"], file_id)

@router.delete("/files/{file_id}")
async def delete_file(file_id: int, Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.delete_file(user["user_id"], file_id)

@router.post("/files/{file_id}")
async def update_file(file_id: int, file: UploadFile = File(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.update_file(user["user_id"], file_id, file)

@router.post("/files/merge")
async def merge_files(file_ids: List[int] = Body(...), Authorization: str = Header(...), file_service: FileService = Depends(get_file_service)):
    user = get_current_user(Authorization)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid token")
    return file_service.merge_files(user["user_id"], file_ids)
