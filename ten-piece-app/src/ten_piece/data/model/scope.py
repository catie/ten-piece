from typing import List

from ten_piece.data.model.record import DataRecord


class Scope(DataRecord):
    scope_id: str
    relevant_tag_types: List[str]

    @property
    def id(self) -> str:
        return self.scope_id
