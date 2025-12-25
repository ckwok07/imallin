class Card:
    def __init__(self, rank, suit) -> None:
        self.rank = rank.value if hasattr(rank, "value") else rank

        self.suit = suit.value if hasattr(suit, "value") else suit