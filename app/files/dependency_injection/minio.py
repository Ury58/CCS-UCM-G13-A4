#app/files/dependency_injection/minio.py

from app.files.persistence.minio import MinioClient

def get_minio_client() -> MinioClient:
    return MinioClient()
