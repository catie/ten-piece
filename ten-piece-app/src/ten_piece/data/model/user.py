from typing import List
from ten_piece.data.model.record import DataRecord


class User(DataRecord):
    user_id: str
    username: str
    tags: List[str]

    @property
    def id(self) -> str:
        return self.user_id
