from ten_piece.client.dynamodb import DynamoDbClient
from ten_piece.model.participant import Participant


class ParticipantDataClient(DynamoDbClient[Participant]):
    def __init__(self):
        super().__init__(table_name_var="CHARACTER_TABLE", model_type=Participant)
