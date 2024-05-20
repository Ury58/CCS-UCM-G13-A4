#app/files/domain/controllers/files/crud/get.py

from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistence.file_bo import FileBOPersistenceInterface


class GetFileDomain:

    def __init__(self, file_persistence_service: FileBOPersistenceInterface):
        self.file_persistence_service = file_persistence_service

    async def __call__(self, input_file_id: int) -> FileBO:
        file_to_return = await self.file_persistence_service.get_file(file_id=input_file_id)
        return file_to_return
