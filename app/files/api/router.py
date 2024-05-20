# # #app/files/api/router.py

# # # import os
# # # from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
# # # from pydantic import BaseModel
# # # from typing import List, Dict
# # # from fastapi.responses import FileResponse
# # # from app.files.domain.services import FileService, get_file_service
# # # from app.files.dependency_injection.redis import get_redis_client
# # # from app.files.persistence.redis import RedisClient

# # # router = APIRouter()

# # # file_names = {}

# # # class FileUrlOutput(BaseModel):
# # #     url: str

# # # @router.get("/file")
# # # async def get_file(service: FileService = Depends(get_file_service)) -> dict:
# # #     files = service.get_all_files("dummy_user")
# # #     return {"files": files}

# # # @router.post("/file")
# # # async def post_file(input: dict, service: FileService = Depends(get_file_service)) -> dict:
# # #     id = len(file_names)
# # #     name = input["name"]
# # #     file_names[name] = id
# # #     return {"id": id}

# # # # @router.get("/file/{id}")
# # # # async def get_file(id: int, service: FileService = Depends(get_file_service)):
# # # #     for current_name, current_id in file_names.items():
# # # #         if current_id == id:
# # # #             filename = current_name
# # # #     return FileResponse(filename, media_type="application/pdf", filename=filename)

# # # @router.get("/file/{id}", response_model=FileUrlOutput)
# # # async def get_file(id: int, service: FileService = Depends(get_file_service)):
# # #     url = service.get_file_url("dummy_user", id)
# # #     return {"url": url}

# # # @router.post("/file/merge")
# # # async def merge_files(input: dict, service: FileService = Depends(get_file_service)) -> dict:
# # #     merged_file = service.merge_files("dummy_user", input["files"])
# # #     return {"id": merged_file["id"]}

# # # @router.post("/file/{id}")
# # # async def post_file(id: int, file: UploadFile = File(), service: FileService = Depends(get_file_service)) -> dict:
# # #     result = service.update_file("dummy_user", id, file) 
# # #     return result

# # # @router.delete("/file/{id}")
# # # async def delete_file(id: int, service: FileService = Depends(get_file_service)) -> dict:
# # #     result = service.delete_file("dummy_user", id)
# # #     return result


# # #app/files/api/router.py

# # import os
# # from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
# # from pydantic import BaseModel
# # from typing import List, Dict
# # from fastapi.responses import FileResponse
# # from tempfile import NamedTemporaryFile
# # from app.files.domain.services import FileService, get_file_service
# # from app.files.dependency_injection.minio import get_minio_client
# # from app.files.persistence.minio import MinioClient

# # router = APIRouter()

# # file_names = {}

# # class FileUrlOutput(BaseModel):
# #     url: str

# # class MergeInput(BaseModel):
# #     files: List[int]
# #     name: str

# # @router.get("/file")
# # async def get_files(service: FileService = Depends(get_file_service)) -> dict:
# #     files = service.get_all_files("dummy_user")
# #     return {"files": files}

# # @router.post("/file")
# # async def post_file(input: dict, service: FileService = Depends(get_file_service)) -> dict:
# #     id = len(file_names)
# #     name = input["name"]
# #     file_names[name] = id
# #     return {"id": id}

# # @router.get("/file/{id}", response_model=FileUrlOutput)
# # async def get_file(id: int, service: FileService = Depends(get_file_service)):
# #     url = service.get_file_url("dummy_user", id)
# #     return {"url": url}

# # @router.post("/file/merge")
# # async def merge_files(input: MergeInput, minio_client: MinioClient = Depends(get_minio_client)) -> dict:
# #     pdfs = [name for name, id in file_names.items() if id in input.files]
# #     merged_pdf_name = input.name
# #     with NamedTemporaryFile(delete=False) as temp_file:
# #         merger = PdfMerger()
# #         for pdf in pdfs:
# #             response = minio_client.get_object(pdf)
# #             temp_file.write(response.read())
# #             merger.append(temp_file.name)
# #         merger.write(temp_file.name)
# #         merger.close()
# #         minio_client.upload_file(open(temp_file.name, "rb"), merged_pdf_name)
# #         os.unlink(temp_file.name)
# #     id = len(file_names)
# #     file_names[merged_pdf_name] = id
# #     return {"id": id}

# # @router.post("/file/{id}")
# # async def post_file(id: int, file: UploadFile = File(), service: FileService = Depends(get_file_service)) -> dict:
# #     result = service.update_file("dummy_user", id, file)
# #     return result

# # @router.delete("/file/{id}")
# # async def delete_file(id: int, service: FileService = Depends(get_file_service)) -> dict:
# #     result = service.delete_file("dummy_user", id)
# #     return result


# import os
# from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
# from pydantic import BaseModel
# from typing import List, Dict
# from fastapi.responses import FileResponse
# from tempfile import NamedTemporaryFile
# from app.files.domain.services import FileService, get_file_service
# from app.files.dependency_injection.minio import get_minio_client
# from app.files.persistence.minio import MinioClient
# from PyPDF2 import PdfMerger

# router = APIRouter()

# file_names = {}

# class FileUrlOutput(BaseModel):
#     url: str

# class MergeInput(BaseModel):
#     files: List[int]
#     name: str

# @router.get("/file")
# async def get_files(service: FileService = Depends(get_file_service)) -> dict:
#     files = service.get_all_files("dummy_user")
#     return {"files": files}

# @router.post("/file")
# async def post_file(input: dict, service: FileService = Depends(get_file_service)) -> dict:
#     id = len(file_names)
#     name = input["name"]
#     file_names[name] = id
#     return {"id": id}

# @router.get("/file/{id}", response_model=FileUrlOutput)
# async def get_file(id: int, service: FileService = Depends(get_file_service)):
#     url = service.get_file_url("dummy_user", id)
#     return {"url": url}

# @router.post("/file/merge")
# async def merge_files(input: MergeInput, minio_client: MinioClient = Depends(get_minio_client)) -> dict:
#     pdfs = [name for name, id in file_names.items() if id in input.files]
#     merged_pdf_name = input.name
#     with NamedTemporaryFile(delete=False) as temp_file:
#         merger = PdfMerger()
#         for pdf in pdfs:
#             response = minio_client.get_object(pdf)
#             temp_file.write(response.read())
#             merger.append(temp_file.name)
#         merger.write(temp_file.name)
#         merger.close()
#         minio_client.upload_file(open(temp_file.name, "rb"), merged_pdf_name)
#         os.unlink(temp_file.name)
#     id = len(file_names)
#     file_names[merged_pdf_name] = id
#     return {"id": id}

# @router.post("/file/{id}")
# async def post_file(id: int, file: UploadFile = File(), service: FileService = Depends(get_file_service)) -> dict:
#     result = service.update_file("dummy_user", id, file)
#     return result

# @router.delete("/file/{id}")
# async def delete_file(id: int, service: FileService = Depends(get_file_service)) -> dict:
#     result = service.delete_file("dummy_user", id)
#     return result


import os
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends
from pydantic import BaseModel
from typing import List, Dict
from fastapi.responses import FileResponse
from tempfile import NamedTemporaryFile
from app.files.domain.services import FileService, get_file_service
from app.files.dependency_injection.minio import get_minio_client
from app.files.persistence.minio import MinioClient
from PyPDF2 import PdfMerger

router = APIRouter()

file_names = {}

class FileUrlOutput(BaseModel):
    url: str

class MergeInput(BaseModel):
    files: List[int]
    name: str

@router.get("/file")
async def get_files(service: FileService = Depends(get_file_service)) -> dict:
    files = service.get_all_files("dummy_user")
    return {"files": files}

@router.post("/file")
async def post_file(input: dict, service: FileService = Depends(get_file_service)) -> dict:
    id = len(file_names)
    name = input["name"]
    file_names[name] = id
    return {"id": id}

@router.get("/file/{id}", response_model=FileUrlOutput)
async def get_file(id: int, service: FileService = Depends(get_file_service)):
    url = service.get_file_url("dummy_user", id)
    return {"url": url}

@router.post("/file/merge")
async def merge_files(input: MergeInput, minio_client: MinioClient = Depends(get_minio_client)) -> dict:
    pdfs = [name for name, id in file_names.items() if id in input.files]
    merged_pdf_name = input.name
    with NamedTemporaryFile(delete=False) as temp_file:
        merger = PdfMerger()
        for pdf in pdfs:
            response = minio_client.get_object(pdf)
            temp_file.write(response.read())
            merger.append(temp_file.name)
        merger.write(temp_file.name)
        merger.close()
        minio_client.upload_file(open(temp_file.name, "rb"), merged_pdf_name)
        os.unlink(temp_file.name)
    id = len(file_names)
    file_names[merged_pdf_name] = id
    return {"id": id}

@router.post("/file/{id}")
async def post_file(id: int, file: UploadFile = File(), service: FileService = Depends(get_file_service)) -> dict:
    result = service.update_file("dummy_user", id, file)
    return result

@router.delete("/file/{id}")
async def delete_file(id: int, service: FileService = Depends(get_file_service)) -> dict:
    result = service.delete_file("dummy_user", id)
    return result
