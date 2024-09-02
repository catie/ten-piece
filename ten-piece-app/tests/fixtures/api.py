import json
from typing import Any, Dict, List, Tuple
from unittest.mock import MagicMock
import pytest

from ten_piece.model.character import Character
from ten_piece.model.user import User


@pytest.fixture
def request_context():
    """Mock Lambda request context"""
    return MagicMock()


@pytest.fixture
def api_request(test_stage, test_account):
    """Generates a test API request"""

    def inner(
        path: str,
        method: str,
        body: Dict[str, Any] = {},
    ) -> dict:
        return {
            "path": path,
            "httpMethod": method,
            "pathParameters": {},
            "queryStringParameters": {},
            "body": json.dumps(body),
            "resource": "/{proxy+}",
            "requestContext": {
                "resourceId": "123456",
                "apiId": "1234567890",
                "resourcePath": "/{proxy+}",
                "httpMethod": method,
                "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
                "accountId": test_account,
                "identity": {
                    "apiKey": "",
                    "userArn": "",
                    "cognitoAuthenticationType": "",
                    "caller": "",
                    "userAgent": "Custom User Agent String",
                    "user": "",
                    "cognitoIdentityPoolId": "",
                    "cognitoIdentityId": "",
                    "cognitoAuthenticationProvider": "",
                    "sourceIp": "127.0.0.1",
                    "accountId": "",
                },
                "stage": test_stage,
            },
            "headers": {
                "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
                "Accept-Language": "en-US,en;q=0.8",
                "CloudFront-Is-Desktop-Viewer": "true",
                "CloudFront-Is-SmartTV-Viewer": "false",
                "CloudFront-Is-Mobile-Viewer": "false",
                "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
                "CloudFront-Viewer-Country": "US",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
                "Upgrade-Insecure-Requests": "1",
                "X-Forwarded-Port": "443",
                "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
                "X-Forwarded-Proto": "https",
                "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
                "CloudFront-Is-Tablet-Viewer": "false",
                "Cache-Control": "max-age=0",
                "User-Agent": "Custom User Agent String",
                "CloudFront-Forwarded-Proto": "https",
                "Accept-Encoding": "gzip, deflate, sdch",
            },
        }

    return inner


@pytest.fixture
def get_user_request(api_request):
    def inner(user_id: str):
        return api_request(
            path=f"/user/{user_id}",
            method="GET",
        )

    return inner


@pytest.fixture
def update_user_request(api_request):
    def inner(user: User):
        return api_request(
            path="/user",
            method="POST",
            body=user.data_record,
        )

    return inner


@pytest.fixture
def get_participant_request(api_request):
    def inner(participant_id: str):
        return api_request(
            path=f"/participant/{participant_id}",
            method="GET",
        )

    return inner


@pytest.fixture
def update_participant_request(api_request):
    def inner(user: User):
        return api_request(
            path="/participant",
            method="POST",
            body=user.data_record,
        )

    return inner


@pytest.fixture
def get_character_request(api_request):
    def inner(character_id: str):
        return api_request(
            path=f"/character/{character_id}",
            method="GET",
        )

    return inner


@pytest.fixture
def update_character_request(api_request):
    def inner(character: Character):
        return api_request(
            path="/character",
            method="POST",
            body=character.data_record,
        )

    return inner
