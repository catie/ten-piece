from typing import Optional, Type

from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.factory.tag import TagFactory
from ten_piece.data.model.ranking import Ranking
from ten_piece.data.model.scope import Scope
from ten_piece.data.model.user import User


class RankingFactory(DataFactory):
    tag_factory: TagFactory = TagFactory()

    @property
    def model_type(self) -> Type:
        return Ranking

    def create_new(self, user: User, scope: Scope) -> Ranking:
        ranking_name = f"{user.display_name} ({scope.display_name})"
        return Ranking(
            ranking_id=user.user_id,
            owner_id=user.user_id,
            scope_id=scope.scope_id,
            display_name=ranking_name,
            ranked_items=[],
            tags=user.tags,
            created_at=user.created_at,
            updated_at=self.current_time,
        )

    def resolve_update(
        self, new_ranking: Ranking, existing_ranking: Optional[Ranking]
    ) -> Ranking:
        if existing_ranking is None:
            return new_ranking

        return Ranking(
            ranking_id=new_ranking.ranking_id,
            owner_id=new_ranking.owner_id,
            tags=self.combine_tags(
                new_tags=new_ranking.tags, existing_tags=existing_ranking.tags
            ),
            scope_id=new_ranking.scope_id,
            display_name=new_ranking.display_name,
            ranked_items=new_ranking.ranked_items,
            created_at=existing_ranking.created_at,
            updated_at=self.current_time,
        )
