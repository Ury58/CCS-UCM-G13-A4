# app/files/persistence/minio.py

from minio import Minio
from minio.error import S3Error

class MinioClient:
    def __init__(self):
        self.client = Minio(
            "minio:9000",
            access_key="YOUR_ACCESS_KEY",
            secret_key="YOUR_SECRET_KEY",
            secure=False
        )
        self.bucket_name = "files"
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def upload_file(self, file, file_name):
        try:
            self.client.put_object(
                self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
            )
            return {"file_name": file_name}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    # Other methods to interact with Minio (e.g., download, delete, list files)
