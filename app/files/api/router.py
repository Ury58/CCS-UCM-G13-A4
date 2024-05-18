#app/files/router.py

from fastapi import APIRouter, HTTPException, UploadFile, File, Header, Body, Path
from pydantic import BaseModel
from typing import Optional, Union, List, Dict
from pypdf import PdfMerger

router = APIRouter()

# class File(BaseModel):
#     name: str
#     author: str
#     amount_of_pages: Optional[int] = None

#     model_config = {
#         json_schema_extra" :{
#         "examples": [
#             {
#                 "name": "File 1",
#                 "author": "Oriol",
#                 "amount_of_pages": 2,
#             },
#             {
#                 "name": "File 2",
#                 "author": "Lucia",
#                 "amount_of_pages": 2,
#             }
#         ]
#         }
#    }

@router.get("/{id}")
async def get_files(id: int, any_name: str = Header(alias="AnyName")) -> File:
    print(any_name)
    return files[id]

@router.post("/")
async def post_files(input_post_file: File) -> dict[str, Union[int, Dict]]:
    new_id = len(files)
    while new_id in files.keys():
        print(new_id)
        new_id += 1
    files[new_id] = input_post_file
    return{
        "id": new_id
    }

@router.post("/merge")
async def post_merge() -> dict:
    file1 ="files/test1"
    file2 ="files/auto"
    
                     