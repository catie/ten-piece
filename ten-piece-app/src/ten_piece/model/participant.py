from typing import List
from ten_piece.model.person import Person
from ten_piece.model.user import User


class Participant(Person):
    participant_id: str
    character_ranking: List[str]

    @property
    def id(self) -> str:
        return self.participant_id

    @classmethod
    def for_user(cls, user: User) -> "Participant":
        return Participant(
            participant_id=user.id,
            display_name=user.display_name,
            gender=user.gender,
            character_ranking=[],
            created_at=user.created_at,
            updated_at=user.updated_at,
        )
