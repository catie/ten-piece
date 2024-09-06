from typing import Optional

from ten_piece.data.factory.factory import DataFactory
from ten_piece.data.model.user import User


class UserFactory(DataFactory):
    def create_new(self, username: str, display_name: str) -> User:
        return User(
            user_id=self.normalize_string(some_string=username),
            username=username,
            display_name=display_name,
            tags=[],
            created_at=self.current_time,
            updated_at=self.current_time,
        )

    def resolve_update(
        self,
        new_user: User,
        existing_user: Optional[User],
    ) -> User:
        if existing_user is None:
            return new_user

        return User(
            user_id=new_user.user_id,
            username=new_user.username,
            display_name=new_user.display_name,
            tags=self.combine_tags(
                new_tags=new_user.tags, existing_tags=existing_user.tags
            ),
            created_at=existing_user.created_at,
            updated_at=self.current_time,
        )
