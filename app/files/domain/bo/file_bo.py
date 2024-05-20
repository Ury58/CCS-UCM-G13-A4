#app/files/domain/bo/file_bo.py

from typing import Optional
from pydantic import BaseModel


class FileBO(BaseModel):
    id: Optional[int] = None
    name: str
    author: str
    amount_of_pages: Optional[int] = None
