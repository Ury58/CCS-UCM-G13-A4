#app/files/domain/services.py

from typing import List, Dict
from fastapi import UploadFile, HTTPException
from app.files.persistence.minio import MinioClient
from app.files.persistence.redis import RedisClient
from fastapi.responses import FileResponse

class FileService:
    def __init__(self, minio_client: MinioClient, redis_client: RedisClient):
        self.minio_client = minio_client
        self.redis_client = redis_client

    def get_all_files(self, user: str) -> List[Dict]:
        files = self.minio_client.list_files()
        return [{"id": i, "name": file} for i, file in enumerate(files)]

    def upload_file(self, user: str, file: UploadFile) -> Dict:
        file_id = len(file_names)
        file_name = file.filename
        self.minio_client.upload_file(file, file_name)
        file_names[file_name] = file_id
        return {"id": file_id}

    def get_file(self, user: str, file_id: int) -> Dict:
        for name, id in file_names.items():
            if id == file_id:
                return FileResponse(name, media_type="application/pdf", filename=name)
        raise HTTPException(status_code=404, detail="File not found")

    def delete_file(self, user: str, file_id: int) -> Dict:
        for name, id in file_names.items():
            if id == file_id:
                self.minio_client.delete_file(name)
                del file_names[name]
                return {"status": "deleted"}
        raise HTTPException(status_code=404, detail="File not found")

    def update_file(self, user: str, file_id: int, file: UploadFile) -> Dict:
        for name, id in file_names.items():
            if id == file_id:
                self.minio_client.upload_file(file, name)
                return {"status": "updated"}
        raise HTTPException(status_code=404, detail="File not found")

    def merge_files(self, user: str, file_ids: List[int]) -> Dict:
        pdfs = [name for name, id in file_names.items() if id in file_ids]
        merged_pdf_name = f"merged_{len(file_names)}.pdf"
        self.minio_client.merge_pdfs(pdfs, merged_pdf_name)
        file_id = len(file_names)
        file_names[merged_pdf_name] = file_id
        return {"id": file_id}

def get_file_service() -> FileService:
    minio_client = MinioClient()
    redis_client = RedisClient()
    return FileService(minio_client, redis_client)
