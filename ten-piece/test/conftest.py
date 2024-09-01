import pytest

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
def environment_base(test_stage, test_account, test_region):
    return {
        "STAGE": test_stage,
        "AWS_ACCOUNT_ID": test_account,
        "AWS_REGION": test_region
    }