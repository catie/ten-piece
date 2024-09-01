from ten_piece.model.person import Person

class Participant(Person):
    participant_id: str

    @property
    def id(self) -> str:
        return self.participant_id