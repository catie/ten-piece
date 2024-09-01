from ten_piece.client.dynamodb import DynamoDbClient
from ten_piece.model.user import User


class UserDataClient(DynamoDbClient[User]):
    def __init__(self):
        super().__init__(table_name_var="CHARACTER_TABLE", model_type=User)
