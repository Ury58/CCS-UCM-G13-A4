#app/files/domain/persistence/file_bo.py

from abc import ABC, abstractmethod

from app.files.domain.bo.file_bo import FileBO


class FileBOPersistenceInterface(ABC):

    @abstractmethod
    async def create_file(self, file: FileBO):
        pass

    @abstractmethod
    async def get_file(self, file_id: int):
        pass
