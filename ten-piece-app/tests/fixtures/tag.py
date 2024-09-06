from typing import Callable, List
import pytest
from ten_piece.data.factory.tag import TagFactory
from ten_piece.data.model.gender import Gender
from ten_piece.data.model.tag import Tag


TEST_TAGS__SPECIES = [
    "species::human",
    "species::reindeer",
]

TEST_TAGS__VITALITY = [
    "vitality::alive",
    "vitality::dead",
    "vitality::undead",
    "vitality::immortal",
    "vitality::resurrected",
    "vitality::non-living",
]

TEST_TAGS__BIRTHPLACE = [
    "birthplace::Wano",
    "birthplace::USA Idaho Boise",
    "birthplace::USA Georgia Atlanta",
    "birthplace::France Paris",
]

TEST_TAGS__BIRTHDATE = [
    "birthdate::january:1",
    "birthdate::february:69",
    "birthdate::march:31",
    "birthdate::april:20",
    "birthdate::may:5",
    "birthdate::june:14",
    "birthdate::july:9",
    "birthdate::august:1",
    "birthdate::september:21",
    "birthdate::october:31",
    "birthdate::november:30",
    "birthdate::december:24",
]

TEST_TAGS__AGE = [
    "age::12",
    "age::range:15-18",
    "age::over:50",
    "age::under:8",
]

TEST_TAGS__GENDER = [
    "gender::male",
    "gender::female",
    "gender::non-binary",
    "gender::none",
]

TEST_TAGS__HAIR_COLOR = [
    "hair-color::black",
    "hair-color::white",
    "hair-color::blonde",
    "hair-color::red",
    "hair-color::brown",
    "hair-color::pink",
    "hair-color::blue",
]

TEST_TAGS__HEIGHT = [
    "height::271",
    "height::range:215-286",
    "height::over:1000",
    "height::under:10",
]

TEST_TAGS__ALIAS = ["alias::Kouzuki Oden", "alias::Gold D Roger"]

TEST_TAGS__AFFILIATIONS = [
    "affiliation::World Marines",
    "affiliation::Big Mom Pirates",
]

TEST_TAGS__OCCUPATION = [
    "occupation::pirate",
    "occupation::marine",
    "occupation::baker",
]

TEST_TAGS__TITLE = [
    "title::King of the Pirates",
    "title::Admiral",
    "title::The Tallest Roller Coaster in South East Rhode Island",
]

TEST_TAGS__ONE_PIECE = [
    "one-piece::d",
    "one-piece::bounty:1-000-000",
    "one-piece::bounty:50",
    "one-piece::devil-fruit",
    "one-piece::devil-fruit:Gum Gum Fruit",
]

TEST_TAGS = [
    *TEST_TAGS__SPECIES,
    *TEST_TAGS__VITALITY,
    *TEST_TAGS__BIRTHPLACE,
    *TEST_TAGS__BIRTHDATE,
    *TEST_TAGS__AGE,
    *TEST_TAGS__GENDER,
    *TEST_TAGS__HAIR_COLOR,
    *TEST_TAGS__HEIGHT,
    *TEST_TAGS__ALIAS,
    *TEST_TAGS__AFFILIATIONS,
    *TEST_TAGS__OCCUPATION,
    *TEST_TAGS__TITLE,
    *TEST_TAGS__ONE_PIECE,
]


@pytest.fixture
def tag_table(data_table):
    return data_table("Tag")


@pytest.fixture
def tag_factory() -> TagFactory:
    return TagFactory()
