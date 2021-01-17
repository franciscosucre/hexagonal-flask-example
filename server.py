from dependency_injector import containers

from container import HexagonalContainer
import sys


class HexagonalServer:
    container: HexagonalContainer


    def __init__(self):
        self.container = HexagonalContainer()
        self.container.config.api_key.from_env('API_KEY')
        self.container.config.timeout.from_env('TIMEOUT')
        self.container.wire(modules=[sys.modules[__name__]])

        main()  # <-- dependency is injected automatically

        with container.api_client.override(mock.Mock()):
            main()  # <-- overridden dependency is injected automatically
