from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

from ten_piece.data.api import DataApi
from ten_piece.core.resolver import RequestResolver
from ten_piece.data.factory.character import CharacterFactory
from ten_piece.data.factory.ranking import RankingFactory
from ten_piece.data.factory.scope import ScopeFactory
from ten_piece.data.factory.tag import TagFactory

app = RequestResolver()

DATA_FACTORIES = [
    CharacterFactory(),
    ScopeFactory(),
    TagFactory(),
    RankingFactory(),
    CharacterFactory(),
]
for factory in DATA_FACTORIES:
    DataApi(app=app, factory=factory)


@app.log.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_HTTP)
def lambda_handler(event, context: LambdaContext):
    return app.resolve(event, context)
