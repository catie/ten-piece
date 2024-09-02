from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from ten_piece.model.user import User
from ten_piece.model.character import Character
from ten_piece.model.participant import Participant
from ten_piece.client.users import UserDataClient
from ten_piece.client.characters import CharacterDataClient
from ten_piece.client.participants import ParticipantDataClient

from ten_piece.api.api import RestApi
from ten_piece.api.resolver import RequestResolver

app = RequestResolver()
user_api = RestApi(
    app=app, api_path="user", data_client=UserDataClient(), model_type=User
)
participant_api = RestApi(
    app=app,
    api_path="participant",
    data_client=ParticipantDataClient(),
    model_type=Participant,
)
character_api = RestApi(
    app=app,
    api_path="character",
    data_client=CharacterDataClient(),
    model_type=Character,
)


@app.log.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
def lambda_handler(event, context: LambdaContext):
    return app.resolve(event, context)
