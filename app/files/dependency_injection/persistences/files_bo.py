#app/files/dependency_injection/persistences/files_bo.py

from dependency_injector import containers, providers

from app.files.persistence.memory_persistence.files_bo import FilesBOMemoryPersistenceService
from app.files.persistence.postgres_persistence.files_bo import FilesBOPostgresPersistenceService


class FilesBOPersistences(containers.DeclarativeContainer):
    postgres = providers.Singleton(
        FilesBOPostgresPersistenceService
    )

    memory = providers.Singleton(
        FilesBOMemoryPersistenceService
    )

    carlemany = postgres
