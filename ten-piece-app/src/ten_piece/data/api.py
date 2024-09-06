from typing import Callable, Generic, Type, TypeVar
from aws_lambda_powertools import Logger
from pydantic import BaseModel

from ten_piece.core.resolver import RequestResolver
from ten_piece.data.client import DataClient
from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.model.record import DataRecord


ModelObject = TypeVar("ModelObject", bound=DataRecord)


class DataApi(BaseModel, Generic[ModelObject]):
    api_path: str

    _app: RequestResolver
    _data_client: DataClient[ModelObject]

    def __init__(self, app: RequestResolver, factory: DataFactory[ModelObject]):
        super().__init__(api_path=factory.entity_type.lower())
        self._app = app
        self._data_client = DataClient(factory=factory)
        self._define_get_()
        self._define_update_()

    @property
    def app(self) -> RequestResolver:
        return self._app

    @property
    def api_name(self) -> str:
        return self.api_path.capitalize()

    @property
    def current_event(self):
        return self._app.current_event

    @property
    def data_client(self):
        return self._data_client

    @property
    def model_type(self) -> Type[ModelObject]:
        return self._data_client.model_type

    @property
    def log(self) -> Logger:
        return self.app.log

    def _define_get_(self) -> Callable[[str], dict]:

        @self.app.get(f"/{self.api_path}/<identifier>")
        def get_item(identifier: str) -> dict:
            if not identifier:
                raise ValueError(f"No {self.api_name} provided")

            self.log.info(f"Looking up {self.api_path} {identifier}")

            result = self._data_client.get_or_none(identifier)

            if result is None:
                raise ValueError(f"{self.api_name} {identifier} not found")

            self.log.info(f"{self.api_name} {identifier} found, returning")
            self.log.debug(result.data_record)

            return result.data_record

        return get_item

    def _define_update_(self) -> Callable[[], dict]:

        @self.app.post(f"/{self.api_path}")
        def update_item() -> dict:
            item = self.app.request_body(self.model_type)

            self.log.info(f"Updating {self.api_path} {item.id}")
            new_item = self.data_client.create_or_update(item)

            self.log.info(f"Successfully updated {self.api_path} {item.id}")
            return new_item.data_record

        return update_item
