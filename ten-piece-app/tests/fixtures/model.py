from datetime import datetime, timedelta, timezone
from random import randint
from typing import List
import pytest

from ten_piece.model.character import Character
from ten_piece.model.gender import Gender
from ten_piece.model.participant import Participant
from ten_piece.model.user import User


_ID_COUNTER = 0


@pytest.fixture
def id_generator():
    def inner():
        global _ID_COUNTER
        _ID_COUNTER = _ID_COUNTER + 1
        return f"id{_ID_COUNTER}"

    return inner


@pytest.fixture
def current_time():
    return datetime.now(tz=timezone.utc)


@pytest.fixture
def previous_time(current_time):
    return current_time - timedelta(days=randint(1, 30))


@pytest.fixture
def build_user(id_generator, current_time, previous_time):
    def inner(username: str, display_name: str, gender: Gender = Gender.UNKNOWN):
        return User(
            user_id=id_generator(),
            username=username,
            display_name=display_name,
            gender=gender,
            created_at=previous_time,
            updated_at=current_time,
        )

    return inner


@pytest.fixture
def build_participant(id_generator, current_time, previous_time):
    def inner(display_name: str, gender: Gender = Gender.UNKNOWN):
        return Participant(
            participant_id=id_generator(),
            display_name=display_name,
            gender=gender,
            character_ranking=[],
            created_at=previous_time,
            updated_at=current_time,
        )

    return inner


@pytest.fixture
def build_character(id_generator, current_time, previous_time):
    def inner(display_name: str, gender: Gender = Gender.UNKNOWN):
        return Character(
            character_id=id_generator(),
            display_name=display_name,
            gender=gender,
            created_at=previous_time,
            updated_at=current_time,
        )

    return inner


@pytest.fixture
def user_catie(build_user):
    return build_user(username="catie", display_name="Catie", gender=Gender.FEMALE)


@pytest.fixture
def user_erin(build_user):
    return build_user(username="eglads", display_name="Erin", gender=Gender.FEMALE)


@pytest.fixture
def participant_jackie(build_participant):
    return build_participant(display_name="Jackie", gender=Gender.FEMALE)


@pytest.fixture
def participant_james(build_participant):
    return build_participant(display_name="James", gender=Gender.NONBINARY)


@pytest.fixture
def character_roger(build_character):
    return build_character(display_name="Gol D. Roger", gender=Gender.MALE)


@pytest.fixture
def character_yamato(build_character):
    return build_character(display_name="Yamato", gender=Gender.NONBINARY)
