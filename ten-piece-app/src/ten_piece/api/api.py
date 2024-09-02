from typing import Callable, Generic, Type
from aws_lambda_powertools import Logger

from ten_piece.client.dynamodb import DynamoDbClient, ModelObject
from ten_piece.api.resolver import RequestResolver


class RestApi(Generic[ModelObject]):
    api_name: str
    api_path: str
    _model_type: Type[ModelObject]
    _data_client: DynamoDbClient[ModelObject]
    _app: RequestResolver
    _logger: Logger

    _get_method: Callable[[str], dict]
    _update_method: Callable[[], str]

    def __init__(
        self,
        app: RequestResolver,
        api_path: str,
        model_type: Type[ModelObject],
        data_client: DynamoDbClient[ModelObject],
    ):
        self.api_name = api_path.capitalize()
        self.api_path = api_path

        self._model_type = model_type
        self._data_client = data_client
        self._app = app

        self._get_method = self._define_get_()
        self._update_method = self._define_update_()

    @property
    def model_type(self):
        return self._model_type

    @property
    def app(self):
        return self._app

    @property
    def current_event(self):
        return self._app.current_event

    @property
    def log(self) -> Logger:
        return self.app.log

    def _define_get_(self) -> Callable[[str], dict]:

        @self.app.get(f"/{self.api_path}/<identifier>")
        def get_item(identifier: str) -> dict:
            if not identifier:
                raise ValueError(f"No {self.api_name} provided")

            self.log.info(f"Attempting to look up {self.api_name} item {identifier}")

            result = self._data_client.get(identifier)

            if result is None:
                raise ValueError(f"{self.api_name} {identifier} not found")

            self.log.info(result.data_record)
            return result.data_record

        return get_item

    def _define_update_(self) -> Callable[[], str]:

        @self.app.post(f"/{self.api_path}")
        def update_item() -> str:
            item = self.app.request_body(self._model_type)
            self.log.info(f"Updating {self.api_name} item {item.id}")
            self._data_client.update(item)
            self.log.info(f"Successfully updated {self.api_name} item {item.id}")
            return item.id

        return update_item
