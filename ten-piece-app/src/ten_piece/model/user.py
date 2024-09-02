from ten_piece.model.person import Person

class User(Person):
    user_id: str
    username: str

    @property
    def id(self) -> str:
        return self.user_id
