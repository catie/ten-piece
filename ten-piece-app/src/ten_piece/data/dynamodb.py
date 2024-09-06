import boto3  # type: ignore

from boto3.dynamodb.table import TableResource  # type: ignore
from typing import Generic, Optional, Type, TypeVar
from pydantic import BaseModel

from ten_piece.core.environment import get_service_environment
from ten_piece.data.model.record import DataRecord

ModelObject = TypeVar("ModelObject", bound=DataRecord)


class DynamoDbClient(BaseModel, Generic[ModelObject]):
    table_name: str
    region: str
    _primary_key: str
    _table: TableResource
    _model_type: Type[ModelObject]

    def __primary_key__(self) -> str:
        for key in self._table.key_schema:  # type: ignore
            if key["KeyType"] == "HASH":
                return key["AttributeName"]
        raise ValueError(f"No primary key found for {self.table_name} table")

    def __init__(
        self,
        model_type: Type[ModelObject],
    ):
        env = get_service_environment()
        table_name = env.load_or_die(f"{model_type.__name__.upper()}_TABLE")
        super().__init__(table_name=table_name, region=env.aws_region)

        self._model_type = model_type
        self._table = boto3.resource("dynamodb", self.region).Table(self.table_name)  # type: ignore
        self._primary_key = self.__primary_key__()

    def put_item(self, item: ModelObject) -> None:
        self._table.put_item(Item=item.data_record)  # type: ignore

    def get_item(self, item_id: str) -> Optional[ModelObject]:
        response = self._table.get_item(Key={self._primary_key: item_id})  # type: ignore
        result = response.get("Item", None)
        if result is None:
            return None
        return self._model_type.model_validate(result)
