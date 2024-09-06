from typing import Callable

from ten_piece.api.api import RestApi
from ten_piece.client.dynamodb import DynamoDbClient
from ten_piece.api.resolver import RequestResolver
from ten_piece.model.participant import Participant
from ten_piece.model.user import User


class UserApi(RestApi[User]):
    _participant_client: DynamoDbClient[Participant]

    def __init__(
        self, app: RequestResolver, participant_client: DynamoDbClient[Participant]
    ):
        super().__init__(app=app, api_path="user", model_type=User)
        self._participant_client = participant_client
        self._define_get_()
        self._define_update_()

    def _define_get_(self) -> Callable[[str], dict]:

        @self.app.get(f"/{self.api_path}/<identifier>")
        def get_item(identifier: str) -> dict:
            if not identifier:
                raise ValueError(f"No {self.api_name} provided")

            self.log.info(f"Attempting to look up {self.api_name} item {identifier}")

            result = self._data_client.get(identifier)

            if result is None:
                raise ValueError(f"{self.api_name} {identifier} not found")

            self.log.info(result.data_record)
            return result.data_record

        return get_item

    def _define_update_(self) -> Callable[[], str]:

        @self.app.post(f"/{self.api_path}")
        def update_item() -> str:
            user = self.app.request_body(self._model_type)
            participant = Participant.for_user(user=user)

            self.log.info(f"Updating user {user.id}")
            self.data_client.update(user)

            self.log.info(f"Updating participant {participant.id}")
            self._participant_client.update(participant)

            self.log.info(f"Successfully updated User {user.id}")
            return user.id

        return update_item
