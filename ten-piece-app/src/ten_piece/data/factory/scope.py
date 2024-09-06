from typing import List, Optional

from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.model.scope import Scope


class ScopeFactory(DataFactory):
    def create_new(
        self, display_name: str, relevant_tag_types: Optional[List[str]] = None
    ) -> Scope:
        return Scope(
            scope_id=self.normalize_string(some_string=display_name),
            display_name=display_name,
            relevant_tag_types=(
                relevant_tag_types if relevant_tag_types is not None else []
            ),
            created_at=self.current_time,
            updated_at=self.current_time,
        )

    def resolve_update(
        self,
        new_scope: Scope,
        existing_scope: Optional[Scope],
    ) -> Scope:
        if existing_scope is None:
            return new_scope

        tag_types = self.updated_supported_types(
            new_types=new_scope.relevant_tag_types,
            existing_types=existing_scope.relevant_tag_types,
        )
        return Scope(
            scope_id=new_scope.scope_id,
            display_name=new_scope.display_name,
            relevant_tag_types=tag_types,
            created_at=self.current_time,
            updated_at=existing_scope.created_at,
        )

    def updated_supported_types(
        self, new_types: List[str], existing_types: List[str]
    ) -> List[str]:

        updated_types = set(existing_types)
        updated_types.update(new_types)

        return list(updated_types)
