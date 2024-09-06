from ten_piece.data.model.tag import TaggedRecord


class Character(TaggedRecord):
    character_id: str

    @property
    def id(self) -> str:
        return self.character_id
