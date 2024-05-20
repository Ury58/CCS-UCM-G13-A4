# #app/files/dependency_injection/domain/files/crud/get.py

# from dependency_injector import containers, providers

# from app.files.dependency_injection.persistences.files_bo import FilesBOPersistences
# from app.files.domain.controllers.files.crud.get import GetFileDomain


# class FilesGetControllers(containers.DeclarativeContainer):
#     v1 = providers.Singleton(
#         GetFileDomain,
#         FilesBOPersistences.carlemany(),
#     )

from dependency_injector import containers, providers
from app.files.dependency_injection.persistences.files_bo import FilesBOPersistences
from app.files.domain.controllers.files.crud.get import GetFileDomain

class FilesGetControllers(containers.DeclarativeContainer):
    v1 = providers.Singleton(
        GetFileDomain,
        FilesBOPersistences.carlemany(),
    )
