import pytest
from unittest import mock

from tests.fixtures.infra import (
    test_stage,
    test_account,
    test_region,
    test_service,
    test_aws_environment,
    build_dynamo_table,
    user_table,
    participant_table,
    character_table,
    service_environment,
)
from tests.fixtures.model import (
    id_generator,
    current_time,
    previous_time,
    build_user,
    build_participant,
    build_character,
    user_catie,
    user_erin,
    participant_james,
    participant_jackie,
    character_roger,
    character_yamato,
)
from tests.fixtures.api import (
    request_context,
    api_request,
    update_user_request,
    get_user_request,
    update_participant_request,
    get_participant_request,
    update_character_request,
    get_character_request,
)


@pytest.fixture(autouse=True)
def test_environment(service_environment):
    with mock.patch.dict("os.environ", service_environment):
        yield
