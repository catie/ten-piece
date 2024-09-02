from typing import Any, List, Optional, Type
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from pydantic import BaseModel


class RequestResolver(APIGatewayRestResolver):
    _logger: Logger = Logger()

    def __init__(self):
        super().__init__()

    @property
    def log(self) -> Logger:
        return self._logger

    def request_body(self, model_type: Type[BaseModel]) -> Any:
        return model_type.model_validate(self.current_event.json_body)

    def get_query_values(self, field_name: str) -> List[str]:
        return self.current_event.get_multi_value_query_string_values(
            field_name, default_values=[]
        )

    def get_path_parameter(self, field_name: str) -> Optional[str]:
        if self.current_event.path_parameters is None:
            return None

        return self.current_event.path_parameters.get(field_name, None)
