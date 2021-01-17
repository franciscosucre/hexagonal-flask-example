from dependency_injector import providers, containers

from domain.services.cat_service import CatService
from domain.usecases.cat_usecases import CatUseCase
from infrastructure.mongodb_adapter import MongoDbAdapter
from infrastructure.repositories.cat_repository import CatRepository
from ui.controllers.cat_controller import CatController
from ui.routes.cat_router import CatRouter


class HexagonalContainer(containers.DeclarativeContainer):
    config = providers.Configuration()

    mongodb = providers.Singleton(MongoDbAdapter)
    cat_repository = providers.Singleton(CatRepository, mongodb=mongodb)
    cat_service = providers.Singleton(CatService, cat_repository=cat_repository)
    cat_use_cases = providers.Singleton(CatUseCase, cat_service=cat_service)
    cat_controller = providers.Singleton(CatController, cat_use_cases=cat_use_cases)
    cat_router = providers.Singleton(CatRouter, cat_controller=cat_controller)
