import pytest

from ten_piece.data.factory.user import UserFactory
from tests.fixtures.user import TEST_USERS


@pytest.mark.parametrize("test_user", TEST_USERS)
def test_valid_users(user_factory: UserFactory, test_user):
    display_name, username, gender = test_user
    user = user_factory.create_new(username=username, display_name=display_name)

    assert user.user_id == user_factory.normalize_string(some_string=username)
