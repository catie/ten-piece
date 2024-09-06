from datetime import datetime
from typing import Dict, Union
from pydantic import (
    AwareDatetime,
    BaseModel,
    ConfigDict,
    field_serializer,
    field_validator,
)


class DataRecord(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    display_name: str
    created_at: AwareDatetime
    updated_at: AwareDatetime

    @property
    def id(self) -> str:
        raise TypeError("Unable to determine record identifier")

    @property
    def name(self) -> str:
        return self.display_name

    @property
    def data_record(self) -> Dict[str, dict]:
        return self.model_dump(by_alias=True, exclude_none=True)

    # @field_validator("created_at", "updated_at")
    # @staticmethod
    # def string_to_date(dt_str: Union[str, datetime], _info) -> datetime:
    #     if isinstance(dt_str, str):
    #         return datetime.fromisoformat(dt_str)
    #     return dt_str

    # @field_serializer("created_at", "updated_at")
    # def date_to_string(self, dt: datetime, _info) -> str:
    #     return dt.isoformat()
