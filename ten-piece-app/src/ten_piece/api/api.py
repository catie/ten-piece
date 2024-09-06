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

    def __init__(
        self,
        app: RequestResolver,
        api_path: str,
        model_type: Type[ModelObject],
    ):
        self._app = app
        self.api_name = api_path.capitalize()
        self.api_path = api_path
        self._model_type = model_type

        table_name_var = f"{api_path.upper()}_TABLE"
        self._data_client = DynamoDbClient[ModelObject](
            table_name_var=table_name_var, model_type=model_type
        )

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
    def data_client(self):
        return self._data_client

    @property
    def log(self) -> Logger:
        return self.app.log
