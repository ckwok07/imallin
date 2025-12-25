from .Suit import Suit
from .Rank import Rank

class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank.value if hasattr(rank, "value") else rank

        self.suit = suit.value if hasattr(suit, "value") else suit

    def display(self) -> str:
        rank_str = Rank(self.rank).display()
        suit_str = Suit(self.suit).display()
        return rank_str + suit_str