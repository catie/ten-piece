from typing import Generic, Optional, Type, TypeVar

from pydantic import BaseModel

from ten_piece.core.error import ServiceError
from ten_piece.data.dynamodb import DynamoDbClient
from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.model.record import DataRecord


ModelObject = TypeVar("ModelObject", bound=DataRecord)


class DataClient(BaseModel, Generic[ModelObject]):
    _factory: DataFactory[ModelObject]
    _data_table: DynamoDbClient[ModelObject]

    def __init__(self, factory: DataFactory[ModelObject]):
        super().__init__()
        self._factory = factory
        self._data_table = DynamoDbClient(model_type=self.model_type)

    @property
    def model_type(self) -> Type[ModelObject]:
        return self._factory.model_type

    @property
    def entity_type(self) -> str:
        return self.model_type.__name__

    def exists(self, item_id: str) -> bool:
        return self.get_or_none(item_id=item_id) is not None

    def get_or_none(self, item_id: str) -> Optional[ModelObject]:
        return self._data_table.get_item(item_id=item_id)

    def get_or_fail(self, item_id: str) -> Optional[ModelObject]:
        item = self.get_or_none(item_id=item_id)
        if item is None:
            raise ServiceError(f"{self.entity_type} {item_id} not found")
        return item

    def create_or_replace(self, item: ModelObject) -> None:
        self._data_table.put_item(item=item)

    def create_or_fail(self, item: ModelObject) -> None:
        if self.exists(item_id=item.id):
            raise ServiceError(f"{self.entity_type} {item.id} already exists")

    def create_or_update(self, item: ModelObject) -> ModelObject:
        existing_item = self.get_or_none(item_id=item.id)
        updated_item = self._factory.resolve_update(
            new_item=item, existing_item=existing_item
        )
        self.create_or_replace(updated_item)
        return updated_item

    def create(self, *args, **kwargs) -> ModelObject:
        new_item = self._factory.create_new(*args, **kwargs)
        self.create_or_fail(new_item)
        return new_item
