from typing import List

from ten_piece.model.gender import Gender
from ten_piece.model.record import DataRecord

class Character(DataRecord):
    character_id: str
    display_name: str
    names: List[str] = []
    genders: List[Gender] = []

    @property
    def id(self) -> str:
        return self.character_id