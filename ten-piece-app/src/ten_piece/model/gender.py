from enum import Enum


class Gender(str, Enum):
    MALE = "Male"
    FEMALE = "Female"
    NONBINARY = "Non-binary"
    NONE = "None"
    UNKNOWN = "Unkown"
