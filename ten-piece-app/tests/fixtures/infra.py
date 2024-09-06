from typing import Callable
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
def build_dynamo_table(
    test_aws_environment, test_stage, test_region
) -> Callable[[str, str], str]:
    def inner(table_name: str, parition_key: str) -> str:
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
def data_table(build_dynamo_table) -> Callable[[str], str]:
    def inner(entity_type: str) -> str:
        return build_dynamo_table(entity_type, f"{entity_type}_id")

    return inner
