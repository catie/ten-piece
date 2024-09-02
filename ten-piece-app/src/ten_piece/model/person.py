from ten_piece.model.gender import Gender
from ten_piece.model.record import DataRecord

class Person(DataRecord):
    display_name: str
    gender: Gender
