import pytest
import boto3
from moto import mock_aws


@pytest.fixture
def test_aws_environment():
    with mock_aws():
        yield


@pytest.fixture
def test_stage():
    return "prod"


@pytest.fixture
def test_account():
    return "123456789012"


@pytest.fixture
def test_region():
    return "us-east-2"


@pytest.fixture
def test_service():
    return "TenPiece"


@pytest.fixture
def build_dynamo_table(test_aws_environment, test_stage, test_region):
    def inner(table_name: str, parition_key: str):
        client = boto3.client("dynamodb", test_region)
        full_table_name = f"{table_name}-{test_stage}"
        client.create_table(
            TableName=full_table_name,
            AttributeDefinitions=[
                {"AttributeName": parition_key, "AttributeType": "S"},
            ],
            KeySchema=[
                {"AttributeName": parition_key, "KeyType": "HASH"},
            ],
            BillingMode="PAY_PER_REQUEST",
        )
        return full_table_name

    return inner


@pytest.fixture
def user_table(build_dynamo_table):
    return build_dynamo_table("users", "user_id")


@pytest.fixture
def participant_table(build_dynamo_table):
    return build_dynamo_table("pariticipants", "participant_id")


@pytest.fixture
def character_table(build_dynamo_table):
    return build_dynamo_table("characters", "character_id")


@pytest.fixture
def service_environment(
    test_stage,
    test_account,
    test_region,
    test_service,
    user_table,
    participant_table,
    character_table,
):
    return {
        "STAGE": test_stage,
        "AWS_ACCOUNT_ID": test_account,
        "AWS_REGION": test_region,
        "POWERTOOLS_SERVICE_NAME": test_service,
        "POWERTOOLS_LOG_LEVEL": "DEBUG",
        "USER_TABLE": user_table,
        "PARTICIPANT_TABLE": participant_table,
        "CHARACTER_TABLE": character_table,
    }
