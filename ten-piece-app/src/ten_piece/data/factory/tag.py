from typing import Optional, Tuple

from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.model.gender import Gender
from ten_piece.data.model.tag import Tag


class TagFactory(DataFactory):

    def gender_tag_id(self, gender: Gender) -> str:
        return f"gender::{gender.value.lower()}"

    def split_tag_string(self, tag_string: str) -> Tuple[str, Optional[str], str]:

        split = tag_string.split("::", 1)
        if len(split) < 2:
            raise ValueError(f"Invalid attribute tag {tag_string}")
        value_split = split[1].split(":", 1)

        tag_type = split[0]

        tag_subtype = value_split[0] if len(value_split) > 1 else None

        tag_value = value_split[1] if len(value_split) > 1 else value_split[0]
        return tag_type, tag_subtype, tag_value

    def normalize_tag_parts(
        self, tag_parts: Tuple[str, Optional[str], str]
    ) -> Tuple[str, Optional[str], str]:

        tag_type, tag_subtype, tag_value = tag_parts

        normalized_type = self.normalize_string(tag_type)
        normalized_subtype = (
            self.normalize_string(tag_subtype) if tag_subtype is not None else None
        )
        normalized_value = self.normalize_string(tag_value)

        return normalized_type, normalized_subtype, normalized_value

    def build_tag_string(self, tag_parts: Tuple[str, Optional[str], str]) -> str:

        tag_type, tag_subtype, tag_value = tag_parts

        if tag_subtype is None or not tag_subtype:
            return f"{tag_type}::{tag_value}"

        return f"{tag_type}::{tag_subtype}:{tag_value}"

    def create_new(self, tag_string: str) -> Tag:
        parts = self.split_tag_string(tag_string=tag_string)
        _, _, original_value = parts

        normalized = self.normalize_tag_parts(parts)
        tag_id = self.build_tag_string(normalized)
        tag_type, tag_subtype, tag_value = normalized

        return Tag(
            tag_id=tag_id,
            display_name=original_value,
            tag_type=tag_type,
            tag_subtype=tag_subtype,
            tag_value=tag_value,
            created_at=self.current_time,
            updated_at=self.current_time,
        )

    def resolve_update(self, new_tag: Tag, existing_tag: Optional[Tag]) -> Tag:

        if existing_tag is None:
            return new_tag

        return Tag(
            tag_id=new_tag.tag_id,
            display_name=new_tag.display_name,
            tag_type=new_tag.tag_type,
            tag_subtype=new_tag.tag_subtype,
            tag_value=new_tag.tag_value,
            created_at=existing_tag.created_at,
            updated_at=self.current_time,
        )
