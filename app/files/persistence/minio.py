# # app/files/persistence/minio.py

# from minio import Minio
# from minio.error import S3Error
# from fastapi import HTTPException, UploadFile

# class MinioClient:
#     def __init__(self):
#         self.client = Minio(
#             "minio:9000",
#             access_key="minio",
#             secret_key="minio123",
#             secure=False
#         )
#         self.bucket_name = "files"
#         if not self.client.bucket_exists(self.bucket_name):
#             self.client.make_bucket(self.bucket_name)

#     def upload_file(self, file: UploadFile, file_name: str):
#         try:
#             self.client.put_object(
#                 self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
#             )
#             return {"file_name": file_name}
#         except S3Error as e:
#             raise HTTPException(status_code=500, detail=str(e))

#     # Other methods to interact with Minio (e.g., download, delete, list files)

from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException, UploadFile

class MinioClient:
    def __init__(self):
        self.client = Minio(
            "minio:9000",
            access_key="minio",
            secret_key="minio123",
            secure=False
        )
        self.bucket_name = "files"
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    def upload_file(self, file: UploadFile, file_name: str):
        try:
            self.client.put_object(
                self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
            )
            return {"file_name": file_name}
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_file(self, file_key: str) -> bytes:
        try:
            response = self.client.get_object(self.bucket_name, file_key)
            return response.read()
        except S3Error as e:
            raise HTTPException(status_code=404, detail="File not found")

    def delete_file(self, file_key: str):
        try:
            self.client.remove_object(self.bucket_name, file_key)
        except S3Error as e:
            raise HTTPException(status_code=404, detail="File not found")
