import pytest

from ten_piece.data.factory.ranking import RankingFactory
from tests.fixtures.scope import TEST_SCOPES
from tests.fixtures.user import TEST_USERS

TEST_RANKINGS = []
for user in TEST_USERS:
    for scope in TEST_SCOPES:
        item = user, scope
        TEST_RANKINGS.append(item)


@pytest.fixture
def ranking_table(data_table):
    return data_table("Ranking")


@pytest.fixture
def ranking_factory() -> RankingFactory:
    return RankingFactory()
