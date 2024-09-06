from typing import List, Optional, Tuple

import pytest

from ten_piece.data.factory.user import UserFactory
from ten_piece.data.model.gender import Gender


TEST_USERS: List[Tuple[str, str, Optional[Gender]]] = [
    ("Catie Yawnelly", "catie", None),
    ("Erin Googlestone", "eglads", Gender.FEMALE),
    ("Jackee Looloos", "jaqui", Gender.FEMALE),
    ("jamesMcK", "Jimmy", Gender.NONBINARY),
    ("Rena", "ace-stan", Gender.NONBINARY),
]


@pytest.fixture
def user_table(data_table):
    return data_table("User")


@pytest.fixture
def user_factory() -> UserFactory:
    return UserFactory()
