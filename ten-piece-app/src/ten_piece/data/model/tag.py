from typing import List, Optional


from ten_piece.data.model.record import DataRecord


class Tag(DataRecord):
    tag_id: str
    tag_type: str
    tag_subtype: Optional[str]
    tag_value: str

    def __str__(self) -> str:
        return self.tag_id

    def __eq__(self, other) -> bool:
        if isinstance(other, Tag):
            return self.tag_id == other.tag_id
        if isinstance(other, str):
            return self.tag_id == other
        raise TypeError(
            f"Cannot compare tag with item of type {other.__class__.__name__}"
        )

    @property
    def id(self) -> str:
        return self.tag_id


class TaggedRecord(DataRecord):
    tags: List[str]
