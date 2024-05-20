#app/files/persistence/postgres_persistence/file_bo.py

from app.files.domain.bo.file_bo import FileBO
from app.files.domain.persistence.file_bo import FileBOPersistenceInterface
from app.files.models import File
from tortoise import transactions

class FileBOPostgresPersistenceService(FileBOPersistenceInterface):

    @transactions.atomic()
    async def create_file(self, file: FileBO):
        new_file = await File.create(
            name=file.name,
            author=file.author,
            amount_of_pages=file.amount_of_pages,
            description=None,
        )
        file.id = new_file.id
        return file.id

    async def get_file(self, file_id: int) -> FileBO:
        file = await File.get(id=file_id)
        return FileBO(
            id=file.id,
            name=file.name,
            author=file.author,
            amount_of_pages=file.amount_of_pages,
        )
