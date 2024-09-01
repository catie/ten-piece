from ten_piece.model.person import Person

class User(Person):
    username: str

    @property
    def id(self) -> str:
        return self.username
