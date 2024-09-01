from typing import List, Optional

from top_ten.character import Character
from top_ten.persisted_model import PersistedModel


class CharacterRanking(PersistedModel):
    """
    This class represents a character ranking for a single person
    """

    name: str
    ranking: List[Character] = []

    def rank(self, character: Character, ranking: Optional[int] = None) -> int:
        if ranking is not None:
            # If a specific ranking is specified, place the character at that position
            # Use ranking - 1 because Python indexing starts at 0 (i.e. the top ranked will be at position 0)
            self.ranking.insert(ranking - 1, character)
        else:
            # If no ranking is provided, place the character at the end of the list
            self.ranking.append(character)

        # Return the total number of characters in the list in case the caller wants to keep track
        return len(self.ranking)
