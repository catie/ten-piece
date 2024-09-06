from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from ten_piece.api.characters import CharacterApi
from ten_piece.api.participants import ParticipantApi
from ten_piece.api.users import UserApi

from ten_piece.api.resolver import RequestResolver

app = RequestResolver()
participant_api = ParticipantApi(app=app)
user_api = UserApi(app=app, participant_client=participant_api.data_client)
character_api = CharacterApi(app=app)


@app.log.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
def lambda_handler(event, context: LambdaContext):
    return app.resolve(event, context)
