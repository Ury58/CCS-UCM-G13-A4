#app/files/domain/services.py

from fastapi import UploadFile, HTTPException
from typing import List, Dict
from app.files.persistence.minio import MinioClient
from app.files.persistence.redis import RedisClient
import json
from pypdf import PdfMerger

class FileService:
    def __init__(self, minio_client: MinioClient, redis_client: RedisClient):
        self.minio_client = minio_client
        self.redis_client = redis_client

    def get_all_files(self, user: str) -> List[Dict]:
        file_keys = self.redis_client.client.keys(f"{user}/*")
        files = []
        for key in file_keys:
            file_metadata = self.redis_client.get(key)
            if file_metadata:
                files.append(json.loads(file_metadata))
        return files

    def upload_file(self, user: str, file: UploadFile) -> Dict:
        file_name = f"{user}/{file.filename}"
        upload_result = self.minio_client.upload_file(file, file_name)
        file_metadata = {
            "user": user,
            "file_name": file.filename,
            "minio_key": file_name
        }
        self.redis_client.set(file_name, json.dumps(file_metadata))
        return {"id": file_name, "name": file.filename}

    def get_file(self, user: str, file_id: int) -> Dict:
        file_key = f"{user}/{file_id}"
        file_metadata = self.redis_client.get(file_key)
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found")
        file_metadata = json.loads(file_metadata)
        file_content = self.minio_client.get_file(file_metadata["minio_key"])
        return {"id": file_id, "name": file_metadata["file_name"], "content": file_content}

    def delete_file(self, user: str, file_id: int) -> Dict:
        file_key = f"{user}/{file_id}"
        file_metadata = self.redis_client.get(file_key)
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found")
        file_metadata = json.loads(file_metadata)
        self.minio_client.delete_file(file_metadata["minio_key"])
        self.redis_client.client.delete(file_key)
        return {"status": "deleted"}

    def update_file(self, user: str, file_id: int, file: UploadFile) -> Dict:
        file_key = f"{user}/{file_id}"
        file_metadata = self.redis_client.get(file_key)
        if not file_metadata:
            raise HTTPException(status_code=404, detail="File not found")
        file_metadata = json.loads(file_metadata)
        self.minio_client.upload_file(file, file_metadata["minio_key"])
        return {"status": "updated"}

    def merge_files(self, user: str, file_ids: List[int]) -> Dict:
        pdf_merger = PdfMerger()
        merged_file_name = f"{user}/merged_file_{len(file_ids)}.pdf"
        for file_id in file_ids:
            file_key = f"{user}/{file_id}"
            file_metadata = self.redis_client.get(file_key)
            if not file_metadata:
                raise HTTPException(status_code=404, detail=f"File with ID {file_id} not found")
            file_metadata = json.loads(file_metadata)
            file_content = self.minio_client.get_file(file_metadata["minio_key"])
            pdf_merger.append(file_content)
        
        with open(merged_file_name, "wb") as output_file:
            pdf_merger.write(output_file)
        
        with open(merged_file_name, "rb") as merged_file:
            self.minio_client.upload_file(merged_file, merged_file_name)
        
        merged_file_metadata = {
            "user": user,
            "file_name": merged_file_name.split('/')[-1],
            "minio_key": merged_file_name
        }
        self.redis_client.set(merged_file_name, json.dumps(merged_file_metadata))
        
        return {"id": merged_file_name, "name": merged_file_name.split('/')[-1]}

def get_file_service() -> FileService:
    minio_client = MinioClient()
    redis_client = RedisClient()
    return FileService(minio_client, redis_client)

