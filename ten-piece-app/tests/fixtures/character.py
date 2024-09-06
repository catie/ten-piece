import pytest

from ten_piece.data.factory.character import CharacterFactory

GOLD_ROGER_TAGS = [
    "alias::Gold Roger",
    "height::range:278-283",
    "hair-color::black",
    "gender::male",
    "occupation::pirate",
    "affiliation::Roger Pirates",
    "title::King of the Pirates",
    "one-piece::d",
]
GOLD_ROGER = ("Gol D. Roger", GOLD_ROGER_TAGS)

YAMATO_TAGS = [
    "alias::Kouzuki Oden",
    "hair-color::white",
    "hair-color::blue",
    "gender::male",
    "gender::female",
    "birthplace::Wano",
    "affiliation::Straw Hat Fleet",
    "hair-color::black",
]
YAMATO = ("Yamato", YAMATO_TAGS)

TEST_CHARACTERS = [GOLD_ROGER, YAMATO]


@pytest.fixture
def character_table(data_table):
    return data_table("Character")



@pytest.fixture
def character_factory() -> CharacterFactory:
    return CharacterFactory()
