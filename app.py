from dependency_injector.providers import Provider
from flask import Flask

import os

from marshmallow import ValidationError
from werkzeug.exceptions import InternalServerError

from container import HexagonalContainer
from infrastructure.errors import marshmallow_error_handler, internal_server_error_handler, HexagonalError, \
    hexagonal_error_handler
from ui.routes.cat_router import CatRouter


class HexagonalApplication:
    _http_server: Flask
    _container: HexagonalContainer

    def __init__(self):
        self._container = HexagonalContainer()
        self._http_server = Flask(__name__)
        self._set_cat_routes()
        self._http_server.register_error_handler(
            InternalServerError,
            internal_server_error_handler
        )
        self._http_server.register_error_handler(
            ValidationError,
            marshmallow_error_handler
        )
        self._http_server.register_error_handler(
            HexagonalError,
            hexagonal_error_handler
        )

    def override_dependencies(self, **overriding_providers: Provider):
        self._container.override_providers(**overriding_providers)

    def listen(self, port: int = 8000):
        self._container.mongodb().connect(os.environ.get('MONGO_URI', 'mongodb://localhost/example'))
        self._http_server.run(port=port)

    def _set_cat_routes(self):
        cat_router: CatRouter = self._container.cat_router()
        routes = cat_router.get_routes()
        for route_pattern, config in routes.items():
            self._http_server.add_url_rule(route_pattern, **config)


application = HexagonalApplication()

if __name__ == "__main__":
    application.listen()
