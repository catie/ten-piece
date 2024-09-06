from typing import Callable

from ten_piece.api.api import RestApi
from ten_piece.api.resolver import RequestResolver
from ten_piece.model.character import Character


class CharacterApi(RestApi[Character]):

    def __init__(self, app: RequestResolver):
        super().__init__(app=app, api_path="character", model_type=Character)
        self._define_get_()
        self._define_update_()

    def _define_get_(self) -> Callable[[str], dict]:

        @self.app.get(f"/{self.api_path}/<identifier>")
        def get_item(identifier: str) -> dict:
            if not identifier:
                raise ValueError(f"No character id provided")

            self.log.info(f"Attempting to look up character {identifier}")

            result = self._data_client.get(identifier)

            if result is None:
                raise ValueError(f"Character {identifier} not found")

            self.log.info(result.data_record)
            return result.data_record

        return get_item

    def _define_update_(self) -> Callable[[], str]:

        @self.app.post(f"/{self.api_path}")
        def update_item() -> str:
            character = self.app.request_body(self._model_type)

            self.log.info(f"Updating character {character.id}")
            self.data_client.update(character)

            self.log.info(f"Successfully updated character {character.id}")
            return character.id

        return update_item
