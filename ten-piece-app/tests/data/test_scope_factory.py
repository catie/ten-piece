import pytest

from ten_piece.data.factory.scope import ScopeFactory
from tests.fixtures.scope import TEST_SCOPES


@pytest.mark.parametrize("test_scope", TEST_SCOPES)
def test_valid_scopes(scope_factory: ScopeFactory, test_scope):
    display_name, tag_types = test_scope
    scope = scope_factory.create_new(display_name=display_name, relevant_tag_types=tag_types)

    assert scope is not None
