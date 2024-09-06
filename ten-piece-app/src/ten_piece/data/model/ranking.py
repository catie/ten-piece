from typing import List


from ten_piece.data.model.tag import TaggedRecord


class Ranking(TaggedRecord):
    ranking_id: str
    owner_id: str
    scope_id: str
    ranked_items: List[TaggedRecord]

    @property
    def id(self) -> str:
        return self.ranking_id
