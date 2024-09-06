from typing import List

from ten_piece.model.person import Person

class Character(Person):
    character_id: str
    names: List[str] = []

    @property
    def id(self) -> str:
        return self.character_id