from typing import List, Optional, Tuple
import pytest

from ten_piece.data.factory.ranking import RankingFactory
from ten_piece.data.factory.scope import ScopeFactory
from ten_piece.data.factory.user import UserFactory
from tests.fixtures.ranking import TEST_RANKINGS


@pytest.mark.parametrize("test_user,test_scope", TEST_RANKINGS)
def test_valid_rankings(
    ranking_factory: RankingFactory,
    user_factory: UserFactory,
    scope_factory: ScopeFactory,
    test_user: Tuple[str, str, Optional[str]],
    test_scope: Tuple[str, List[str]],
):
    user_display, username, _ = test_user
    user = user_factory.create_new(display_name=user_display, username=username)
    scope_name, tag_types = test_scope
    scope = scope_factory.create_new(
        display_name=scope_name, relevant_tag_types=tag_types
    )

    ranking = ranking_factory.create_new(user=user, scope=scope)
    assert ranking.display_name == f"{user.display_name} ({scope.display_name})"
