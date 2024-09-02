import json
from ten_piece.model.character import Character
from ten_piece.model.participant import Participant
from ten_piece.model.user import User


def execute_api_test(update_request, get_request, request_context, model_object):
    from ten_piece import app

    ret = app.lambda_handler(update_request(model_object), request_context)
    assert ret["statusCode"] == 200

    ret = app.lambda_handler(get_request(model_object.id), request_context)
    assert ret["statusCode"] == 200

    return json.loads(ret["body"])


def test_user_api(
    test_environment, update_user_request, get_user_request, request_context, user_catie
):
    result = execute_api_test(
        update_user_request, get_user_request, request_context, user_catie
    )
    actual_user = User.model_validate(result)
    assert user_catie.user_id == actual_user.user_id
    assert user_catie.username == actual_user.username
    assert user_catie.display_name == actual_user.display_name


def test_participant_api(
    test_environment,
    update_participant_request,
    get_participant_request,
    request_context,
    participant_james,
):
    result = execute_api_test(
        update_participant_request,
        get_participant_request,
        request_context,
        participant_james,
    )
    actual_participant = Participant.model_validate(result)
    assert participant_james.id == actual_participant.id
    assert participant_james.participant_id == actual_participant.participant_id
    assert participant_james.display_name == actual_participant.display_name


def test_character_api(
    test_environment,
    update_character_request,
    get_character_request,
    request_context,
    character_roger,
):
    result = execute_api_test(
        update_character_request,
        get_character_request,
        request_context,
        character_roger,
    )
    actual_character = Character.model_validate(result)
    assert character_roger.id == actual_character.id
    assert character_roger.character_id == actual_character.character_id
    assert character_roger.display_name == actual_character.display_name
