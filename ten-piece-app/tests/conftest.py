import pytest
from unittest import mock

from tests.fixtures.infra import *
from tests.fixtures.character import *
from tests.fixtures.ranking import *
from tests.fixtures.scope import *
from tests.fixtures.user import *
from tests.fixtures.tag import *

pytest_plugins = [
    "tests.fixtures.infra",
    "tests.fixtures.character",
    "tests.fixtures.ranking",
    "tests.fixtures.scope",
    "tests.fixtures.user",
    "tests.fixtures.tag",
]


@pytest.fixture
def service_environment(
    test_stage,
    test_account,
    test_region,
    test_service,
    user_table,
    character_table,
    ranking_table,
    scope_table,
    tag_table,
):
    return {
        "STAGE": test_stage,
        "AWS_ACCOUNT_ID": test_account,
        "AWS_REGION": test_region,
        "POWERTOOLS_SERVICE_NAME": test_service,
        "POWERTOOLS_LOG_LEVEL": "DEBUG",
        "USER_TABLE": user_table,
        "CHARACTER_TABLE": character_table,
        "RANKING_TABLE": ranking_table,
        "SCOPE_TABLE": scope_table,
        "TAG_TABLE": tag_table,
    }


@pytest.fixture(autouse=True)
def test_environment(service_environment):
    with mock.patch.dict("os.environ", service_environment):
        yield
