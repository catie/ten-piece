from typing import List, Optional


from ten_piece.data.model.character import Character
from ten_piece.data.factory.tag import TagFactory
from ten_piece.data.factory.factory import DataFactory


class CharacterFactory(DataFactory):
    tag_factory: TagFactory = TagFactory()

    def create_new(
        self, display_name: str, tags: Optional[List[str]] = None
    ) -> Character:

        char_tags = tags if tags is not None else []
        return Character(
            character_id=self.normalize_string(some_string=display_name),
            display_name=display_name,
            tags=char_tags,
            created_at=self.current_time,
            updated_at=self.current_time,
        )

    def resolve_update(
        self,
        new_character: Character,
        existing_character: Optional[Character],
    ) -> Character:
        if existing_character is None:
            return new_character

        return Character(
            character_id=new_character.character_id,
            display_name=new_character.display_name,
            tags=new_character.tags,
            created_at=existing_character.created_at,
            updated_at=self.current_time,
        )
