# # # app/files/persistence/minio.py

# # # from minio import Minio
# # # from minio.error import S3Error
# # # from fastapi import HTTPException
# # # from pypdf import PdfMerger
# # # from typing import List
# # # from tempfile import NamedTemporaryFile
# # # import os

# # # class MinioClient:
# # #     def __init__(self):
# # #         self.client = Minio(
# # #             "minio-server:9000",
# # #             access_key="minio",
# # #             secret_key="minio123",
# # #             secure=False
# # #         )
# # #         self.bucket_name = "files"
# # #         if not self.client.bucket_exists(self.bucket_name):
# # #             self.client.make_bucket(self.bucket_name)

# # #     def upload_file(self, file, file_name):
# # #         try:
# # #             self.client.put_object(
# # #                 self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
# # #             )
# # #             return {"file_name": file_name}
# # #         except S3Error as e:
# # #             raise HTTPException(status_code=500, detail=str(e))

# # #     def merge_pdfs(self, pdfs: List[str], output_name: str):
# # #         merger = PdfMerger()
# # #         for pdf in pdfs:
# # #             response = self.client.get_object(self.bucket_name, pdf)
# # #             with NamedTemporaryFile(delete=False) as temp_file:
# # #                 temp_file.write(response.read())
# # #                 merger.append(temp_file.name)
# # #                 os.unlink(temp_file.name)
# # #         with NamedTemporaryFile(delete=False) as temp_file:
# # #             merger.write(temp_file.name)
# # #             merger.close()
# # #             with open(temp_file.name, "rb") as temp_merged:
# # #                 self.upload_file(temp_merged, output_name)
# # #             os.unlink(temp_file.name)

# # #     def list_files(self) -> List[str]:
# # #         objects = self.client.list_objects(self.bucket_name)
# # #         return [obj.object_name for obj in objects]

# # #     def delete_file(self, file_name: str):
# # #         try:
# # #             self.client.remove_object(self.bucket_name, file_name)
# # #         except S3Error as e:
# # #             raise HTTPException(status_code=500, detail=str(e))

# # #     def get_file_url(self, file_name: str) -> str:
# # #         try:
# # #             url = self.client.presigned_get_object(self.bucket_name, file_name)
# # #             return url
# # #         except S3Error as e:
# # #             raise HTTPException(status_code=500, detail=str(e))

# # #     # Other methods to interact with Minio (e.g., download, delete, list files)

# # from minio import Minio
# # from minio.error import S3Error
# # from fastapi import HTTPException
# # from tempfile import NamedTemporaryFile
# # from typing import List
# # import os

# # class MinioClient:
# #     def __init__(self):
# #         self.client = Minio(
# #             "minio-server:9000",
# #             access_key="minio",
# #             secret_key="minio123",
# #             secure=False
# #         )
# #         self.bucket_name = "files"
# #         if not self.client.bucket_exists(self.bucket_name):
# #             self.client.make_bucket(self.bucket_name)

# #     def upload_file(self, file, file_name):
# #         try:
# #             self.client.put_object(
# #                 self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
# #             )
# #             return {"file_name": file_name}
# #         except S3Error as e:
# #             raise HTTPException(status_code=500, detail=str(e))

# #     def list_files(self) -> List[str]:
# #         objects = self.client.list_objects(self.bucket_name)
# #         return [obj.object_name for obj in objects]

# #     def delete_file(self, file_name: str):
# #         try:
# #             self.client.remove_object(self.bucket_name, file_name)
# #         except S3Error as e:
# #             raise HTTPException(status_code=500, detail=str(e))

# #     def get_file_url(self, file_name: str) -> str:
# #         try:
# #             url = self.client.presigned_get_object(self.bucket_name, file_name)
# #             return url
# #         except S3Error as e:
# #             raise HTTPException(status_code=500, detail=str(e))

# #     def get_object(self, file_name: str):
# #         try:
# #             return self.client.get_object(self.bucket_name, file_name)
# #         except S3Error as e:
# #             raise HTTPException(status_code=500, detail=str(e))


# from minio import Minio
# from minio.error import S3Error
# from fastapi import HTTPException
# from tempfile import NamedTemporaryFile
# from typing import List
# import os

# class MinioClient:
#     def __init__(self):
#         self.client = Minio(
#             "minio-server:9000",
#             access_key="minio",
#             secret_key="minio123",
#             secure=False
#         )
#         self.bucket_name = "files"
#         if not self.client.bucket_exists(self.bucket_name):
#             self.client.make_bucket(self.bucket_name)

#     def upload_file(self, file, file_name):
#         try:
#             self.client.put_object(
#                 self.bucket_name, file_name, file.file, length=-1, part_size=10*1024*1024
#             )
#             return {"file_name": file_name}
#         except S3Error as e:
#             raise HTTPException(status_code=500, detail=str(e))

#     def list_files(self) -> List[str]:
#         objects = self.client.list_objects(self.bucket_name)
#         return [obj.object_name for obj in objects]

#     def delete_file(self, file_name: str):
#         try:
#             self.client.remove_object(self.bucket_name, file_name)
#         except S3Error as e:
#             raise HTTPException(status_code=500, detail=str(e))

#     def get_file_url(self, file_name: str) -> str:
#         try:
#             url = self.client.presigned_get_object(self.bucket_name, file_name)
#             return url
#         except S3Error as e:
#             raise HTTPException(status_code=500, detail=str(e))

#     def get_object(self, file_name: str):
#         try:
#             return self.client.get_object(self.bucket_name, file_name)
#         except S3Error as e:
#             raise HTTPException(status_code=500, detail=str(e))


from minio import Minio
from minio.error import S3Error
from fastapi import HTTPException
from tempfile import NamedTemporaryFile
from typing import List
import os

class MinioClient:
    def __init__(self):
        self.client = Minio(
            "minio-server:9000",
            access_key="minio",
            secret_key="minio123",
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

    def list_files(self) -> List[str]:
        objects = self.client.list_objects(self.bucket_name)
        return [obj.object_name for obj in objects]

    def delete_file(self, file_name: str):
        try:
            self.client.remove_object(self.bucket_name, file_name)
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_file_url(self, file_name: str) -> str:
        try:
            url = self.client.presigned_get_object(self.bucket_name, file_name)
            return url
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))

    def get_object(self, file_name: str):
        try:
            return self.client.get_object(self.bucket_name, file_name)
        except S3Error as e:
            raise HTTPException(status_code=500, detail=str(e))
