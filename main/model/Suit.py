from enum import Enum

# a class to represent a card suit
class Suit(Enum):
    DIAMONDS = 0
    CLUBS = 1
    HEARTS = 2
    SPADES = 3

    # displays a suit
    def display(self) -> str:
        return {
            Suit.CLUBS: "c",
            Suit.DIAMONDS: "d",
            Suit.HEARTS: "h",
            Suit.SPADES: "s"}[self]  