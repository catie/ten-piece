import pytest

from ten_piece.data.factory.scope import ScopeFactory


ONE_PIECE__SUPPORTED_TYPES = [
    "height",
    "hair-color",
    "birthplace",
    "birthdate",
    "one-piece",
    "title",
    "affiliation",
    "organization",
]
ONE_PIECE = ("One Piece", ONE_PIECE__SUPPORTED_TYPES)

ROLLER_COASTERS__SUPPORTED_TYPES = [
    "height",
    "location",
]
ROLLER_COASTERS = ("Roller Coasters", ROLLER_COASTERS__SUPPORTED_TYPES)

TEST_SCOPES = [ONE_PIECE, ROLLER_COASTERS]


@pytest.fixture
def scope_table(data_table):
    return data_table("Scope")


@pytest.fixture
def scope_factory() -> ScopeFactory:
    return ScopeFactory()
