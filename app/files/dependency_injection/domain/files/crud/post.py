# #app/files/dependency_injection/domain/files/crud/post.py

# from dependency_injector import containers, providers

# from app.files.dependency_injection.persistences.files_bo import FilesBOPersistences
# from app.files.domain.controllers.files.crud.post import PostFileDomain


# class FilesPostControllers(containers.DeclarativeContainer):
#     v1 = providers.Singleton(
#         PostFileDomain,
#         files_persistence_service=FilesBOPersistences.carlemany(),
#     )

from dependency_injector import containers, providers
from app.files.dependency_injection.persistences.files_bo import FilesBOPersistences
from app.files.domain.controllers.files.crud.post import PostFileDomain

class FilesPostControllers(containers.DeclarativeContainer):
    v1 = providers.Singleton(
        PostFileDomain,
        files_persistence_service=FilesBOPersistences.carlemany(),
    )
