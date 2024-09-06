import pytest

from ten_piece.data.factory.character import CharacterFactory
from tests.fixtures.character import TEST_CHARACTERS


@pytest.mark.parametrize("test_character", TEST_CHARACTERS)
def test_valid_characters(character_factory: CharacterFactory, test_character):
    display_name, tags = test_character
    character = character_factory.create_new(display_name=display_name, tags=tags)

    assert character.character_id == character_factory.normalize_string(
        some_string=display_name
    )
