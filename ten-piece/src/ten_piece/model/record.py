from datetime import datetime, timezone
from typing import Annotated, Any, Callable, Dict, Optional
from pydantic import BaseModel, ConfigDict, Field, PlainSerializer


class DataRecord(BaseModel):
    model_config = ConfigDict()

    @property
    def id(self) -> str:
        raise TypeError("Unable to determine record identifier")

    @property
    def data_record(self) -> Dict[str, dict]:
        return self.model_dump()

    @staticmethod
    def date_field(default_factory: Optional[Callable[[], Any]] = None):
        current_time = lambda: datetime.now(timezone.utc)
        factory = default_factory if default_factory is not None else current_time
        return Annotated[
            Field(default_factory=factory),
            PlainSerializer(lambda dt: dt.isoformat(), return_type=str),
        ]
