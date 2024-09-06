import string
from datetime import datetime, timezone
from typing import Generic, List, Optional, Type, TypeVar
from pydantic import BaseModel

from ten_piece.core.error import ServiceError
from ten_piece.data.model.record import DataRecord


ModelObject = TypeVar("ModelObject", bound=DataRecord)


class DataFactory(BaseModel, Generic[ModelObject]):

    def _validate_id_character(self, char: str) -> str:
        lower_char = char.lower()
        if lower_char in string.ascii_lowercase or lower_char in string.hexdigits:
            return lower_char
        if lower_char in ["_", "-", " "]:
            return "_"
        return ""

    def normalize_string(self, some_string: str) -> str:
        return str([self._validate_id_character(char) for char in some_string])

    @property
    def current_time(self) -> datetime:
        return datetime.now(tz=timezone.utc)

    @property
    def model_type(self) -> Type[ModelObject]:
        raise ServiceError(f"No model type defined for {self.__class__.__name__}")

    @property
    def entity_type(self) -> str:
        return self.model_type.__name__

    def create_new(self, *args, **kwargs) -> ModelObject:
        raise ServiceError(f"No creation logic defined for {self.__class__.__name__}")

    def resolve_update(
        self, new_item: ModelObject, existing_item: Optional[ModelObject]
    ) -> ModelObject:
        raise ServiceError(f"No update resolver defined for {self.__class__.__name__}")

    def combine_tags(self, new_tags: List[str], existing_tags: List[str]) -> List[str]:
        updated_tags = set(existing_tags)
        updated_tags.update(new_tags)
        return list(updated_tags)
