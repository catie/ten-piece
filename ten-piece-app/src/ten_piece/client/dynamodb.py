import boto3

from boto3.dynamodb.table import TableResource
from typing import Generic, Optional, Type, TypeVar
from pydantic import BaseModel

from ten_piece.environment import get_service_environment
from ten_piece.model.record import DataRecord

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
        table_name_var: str,
        model_type: Type[ModelObject],
    ):
        env = get_service_environment()
        table_name = env.load_or_die(table_name_var)
        super().__init__(table_name=table_name, region=env.aws_region)

        self._model_type = model_type
        self._table = boto3.resource("dynamodb", self.region).Table(self.table_name)  # type: ignore
        self._primary_key = self.__primary_key__()

    def update(self, record: ModelObject) -> None:
        print(record.data_record)
        self._table.put_item(Item=record.data_record)  # type: ignore

    def get(self, record_id: str) -> Optional[ModelObject]:
        print({self._primary_key: record_id})
        response = self._table.get_item(Key={self._primary_key: record_id})  # type: ignore
        print(response)
        result = response.get("Item", None)
        if result is None:
            return None
        return self._model_type.model_validate(result)
